import openpyxl
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import csv
import xlwt
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from openpyxl.utils import get_column_letter
from openpyxl.workbook import Workbook
from openpyxl.worksheet.dimensions import ColumnDimension
from openpyxl.styles import Font

from .forms import CadastroClienteForm, VeiculoForm, CriarOrcamentoForm
from .models import Cliente, Veiculo, OrcamentoNaoAprovado, OrdemServicoAberta
from django.db.models import F, Count


def clientes(request):
    form = CadastroClienteForm()
    clientes = Cliente.objects.all()  # Obtenha todos os clientes

    clientes_com_veiculo = []
    for cliente in clientes:
        veiculos = Veiculo.objects.filter(cliente=cliente)
        if veiculos.exists():
            clientes_com_veiculo.append({
                'cliente': cliente,
                'veiculos': veiculos
            })
    qtd_clientes = len(clientes_com_veiculo)

    return render(request, 'pages/clientes.html', {'form': form,
                                                   'clientes_com_veiculo': clientes_com_veiculo,
                                                   'qtd_clientes': qtd_clientes})

def clientes_lista(request):
    form = CadastroClienteForm()
    queryset = Cliente.objects.select_related('veiculo')\
                                                        .values(
                                                               'id',
                                                                'nome',
                                                                'telefone',
                                                                'email',
                                                                'veiculo__marca',
                                                                'veiculo__modelo',
                                                                'veiculo__placa'
                                                                )
    result_list = list(queryset)

    clientes_com_carro = []

    for item in result_list:
        if item['veiculo__placa']:
            clientes_com_carro.append(item)

    return JsonResponse({
        'clientes_com_carro': clientes_com_carro,
        })

def cadastro_clientes(request):
    if request.method == "POST":
        form = CadastroClienteForm(request.POST)
        veiculo_form = VeiculoForm(request.POST)

        if form.is_valid() and veiculo_form.is_valid():
            cliente = form.save()

            numero_de_carros = request.POST.get('numero_de_carros', 1)
            for _ in range(int(numero_de_carros)):
                veiculo = veiculo_form.save(commit=False)
                veiculo.cliente = cliente
                veiculo.save()

            return redirect('clientes')
    else:
        form = CadastroClienteForm()
        veiculo_form = VeiculoForm()

    context = {
        'form': form,
        'veiculo_form': veiculo_form
    }

    return render(request, 'pages/cadastro_clientes.html', context)

def informacoes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    veiculos = Veiculo.objects.filter(cliente=cliente)

    cliente_detalhes = {
        'nome': cliente.nome,
        'cpf': cliente.cpf,
        'telefone': cliente.telefone,
        'email': cliente.email,
        'veiculos': [{'modelo': veiculo.modelo, 'placa': veiculo.placa} for veiculo in veiculos]
    }

    return JsonResponse({'cliente_detalhes': cliente_detalhes})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    veiculos = Veiculo.objects.filter(cliente=cliente)

    if request.method == 'POST':
        form = CadastroClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()

            for veiculo in veiculos:
                veiculo_form = VeiculoForm(request.POST,
                                           instance=veiculo)
                if veiculo_form.is_valid():
                    veiculo_form.save()
            return redirect('editar_cliente', cliente_id=cliente.id)
    else:
        form = CadastroClienteForm(instance=cliente)
        veiculo_forms = [VeiculoForm(instance=veiculo) for veiculo in veiculos]

    return render(request, 'pages/editar_cliente.html', {'form': form, 'veiculo_forms': veiculo_forms})

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()

    id_cliente = cliente_id
    return redirect(reverse('clientes') + f'?aba=att_cliente&id_cliente={id_cliente}')

def exportar_clientes(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="clientes_com_carro.xlsx"'

    wb = Workbook()
    ws = wb.active

    row_num = 1  # Comece da primeira linha, pois a primeira linha contém os títulos das colunas

    bold_font = Font(bold=True)
    bold_style = "bold"  # Não é necessário criar um estilo para negrito

    columns = ['Nome', 'CPF', 'Telefone', 'Email', 'Marca do Carro', 'Modelo do Carro', 'Placa do Carro']

    # Crie uma lista para rastrear a largura máxima de cada coluna
    column_widths = [len(column_title) for column_title in columns]

    for col_num, column_title in enumerate(columns, 1):
        cell = ws.cell(row=row_num, column=col_num, value=column_title)
        cell.font = bold_font
        # Atualize a largura máxima da coluna com base no título
        column_widths[col_num - 1] = max(column_widths[col_num - 1], len(column_title))

    clientes_com_carro = Cliente.objects.filter(veiculo__isnull=False).distinct()

    for cliente in clientes_com_carro:
        veiculos = Veiculo.objects.filter(cliente=cliente)
        for veiculo in veiculos:
            row_num += 1
            row = [
                cliente.nome,
                cliente.cpf,
                cliente.telefone,
                cliente.email,
                veiculo.marca,
                veiculo.modelo,
                veiculo.placa
            ]
            for col_num, cell_value in enumerate(row, 1):
                cell = ws.cell(row=row_num, column=col_num, value=cell_value)
                # Atualize a largura máxima da coluna com base no conteúdo da célula
                column_widths[col_num - 1] = max(column_widths[col_num - 1], len(str(cell_value)))

    # Ajuste a largura de cada coluna de acordo com a largura máxima
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = (width + 2)  # Adicione um espaço extra

    wb.save(response)
    return response

def novo_orcamento(request):
    form = CadastroClienteForm()
    clientes = Cliente.objects.all()
    total_orcamentos = OrcamentoNaoAprovado.objects.count()

    clientes_com_veiculo = []
    for cliente in clientes:
        veiculos = Veiculo.objects.filter(cliente=cliente)
        if veiculos.exists():
            clientes_com_veiculo.append({
                'cliente': cliente,
                'veiculos': veiculos
            })
    context = {
        'form': form,
        'clientes': clientes,
        'clientes_com_veiculo': clientes_com_veiculo,  # Remova o espaço extra aqui
        'total_orcamentos': total_orcamentos
    }

    return render(request, 'pages/novo_orcamento.html', context)

def contar_orcamentos_nao_aprovados(request):
    clientes_com_orcamentos = Cliente.objects.filter(
        orcamentonaoaprovado__isnull=False
    ).annotate(
        num_orcamentos_nao_aprovados=Count('orcamentonaoaprovado')
    ).values(
        'id',
        'nome',
        'veiculo__marca',
        'veiculo__modelo',
        'veiculo__placa',
        'num_orcamentos_nao_aprovados'
    )
    return JsonResponse({'clientes': clientes})

def criar_orcamento(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    veiculo = Veiculo.objects.filter(cliente=cliente).first()  # Obtém o primeiro veículo associado ao cliente

    if request.method == 'POST':
        form = CriarOrcamentoForm(request.POST)
        if form.is_valid():
            orcamento = form.save(commit=False)
            orcamento.cliente = cliente
            orcamento.veiculo = veiculo
            orcamento.save()

            total_orcamentos = OrcamentoNaoAprovado.objects.count()
            messages.success(request, 'Orçamento criado com sucesso!', extra_tags='success', fail_silently=True)
            return redirect('orcamentos_abertos')  # Redirecione para uma página de sucesso após a criação do orçamento
    else:
        form = CriarOrcamentoForm(initial={'cliente': cliente})
    return render(request, 'pages/criar_orcamento.html', {'form': form, 'cliente': cliente, 'veiculo': veiculo})

def orcamentos_lista(request):
    clientes_com_orcamentos = Cliente.objects.filter(
        orcamentonaoaprovado__isnull=False
    ).annotate(
        num_orcamentos_nao_aprovados=Count('orcamentonaoaprovado')
    ).prefetch_related('veiculo', 'orcamentonaoaprovado').values(
        'id',
        'nome',
        'cpf',
        'telefone',
        'email',
        'veiculo__modelo',
        'veiculo__placa',
        'orcamentonaoaprovado__valor_estimado'
    )

    clientes_orcamentos = list(clientes_com_orcamentos)
    return render(request, 'pages/orcamentos_abertos.html', {'clientes': clientes_com_orcamentos})


def orcamentos_abertos(request):
    queryset = OrcamentoNaoAprovado.objects.filter(numero_orcamento__isnull=False)\
                                           .values(
                                               'id',
                                               'numero_orcamento',
                                               'cliente__nome',
                                               'cliente__cpf',
                                               'cliente__telefone',
                                               'cliente__email',
                                               'cliente__veiculo__marca',
                                               'cliente__veiculo__modelo',
                                               'cliente__veiculo__placa',
                                               'valor_estimado'
                                           )
    result_list = list(queryset)
    orcamentos_com_numero = []

    for item in result_list:
        orcamentos_com_numero.append(item)

    orcamentos_com_numero = list(queryset)

    return render(request, 'pages/orcamentos_abertos.html', {'orcamentos_com_numero': orcamentos_com_numero})


def excluir_orcamento(request, orcamento_id):
    orcamento = get_object_or_404(OrcamentoNaoAprovado, id=orcamento_id)
    orcamento.delete()

    # Redirecionar para a página de lista de orçamentos ou onde você preferir
    return redirect(reverse('orcamentos_abertos'))



# Função para aprovar orçamento e encaminhar para Ordem de Serviço em aberto
def os_aberta(request, orcamento_id):
    orcamento = OrcamentoNaoAprovado.objects.get(id=orcamento_id)

    ordem_aberta = orcamento.criar_ordem_servico_aberta()

    orcamento.delete()

    messages.success(request, 'Orçamento foi aprovado. Ordem de serviço iniciada! ', extra_tags='success', fail_silently=True)
    return redirect(reverse('ordem_servico'))

def ordem_servico(request):
    query_ordem = OrdemServicoAberta.objects.values('numero_ordem',
                                                    'data_ordem',
                                                    'servico',
                                                    'valor_estimado',
                                                    'cliente__nome',
                                                    'cliente__cpf',
                                                    'cliente__telefone',
                                                    'cliente__email',
                                                    'cliente__endereco',
                                                    'cliente__veiculo__marca',
                                                    'cliente__veiculo__modelo',
                                                    'cliente__veiculo__placa',
                                                    'cliente__veiculo__ano',
                                                    )
    result_query =[]

    for ordem in query_ordem:
        result_query.append(ordem)

    num_items = len(result_query)

    context = {
        'result_query': result_query,
        'num_items': num_items,
    }
    return render(request, 'pages/os_aberta.html', context)

def ordem_lista(request):
    query_ordem = OrdemServicoAberta.objects.values('numero_ordem',
                                                    'data_ordem',
                                                    'servico',
                                                    'valor_estimado',
                                                    'cliente__nome',
                                                    'cliente__cpf',
                                                    'cliente__telefone',
                                                    'cliente__email',
                                                    'cliente__endereco',
                                                    'cliente__veiculo__marca',
                                                    'cliente__veiculo__modelo',
                                                    'cliente__veiculo__placa',
                                                    'cliente__veiculo__ano',
                                                    )
    result_query = []

    for ordem in query_ordem:
        result_query.append(ordem)


    return JsonResponse({'result_query': result_query})