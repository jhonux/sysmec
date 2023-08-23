# from django.db.models import Q
# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
#
# from .models import Cliente, OrcamentoNaoAprovado, Veiculo
# from .forms import NovoOrcamentoForm
# #
# def novo_orcamento(request):
#     form = NovoOrcamentoForm()
#     clientes = Cliente.objects.all()  # Certifique-se de importar o modelo Cliente
#
#     context = {
#         'form': form,
#         'clientes': clientes,
#     }
#
#     return render(request, 'novo_orcamento.html', context)
#
# def buscar_cliente_por_nome(request):
#     if request.method == 'GET':
#         nome_cliente = request.GET.get('nome_cliente', '')
#
#         try:
#             cliente = Cliente.objects.get(nome__icontains=nome_cliente)
#             veiculo = cliente.veiculo_set.first()  # Suponha que o cliente tenha um único veículo
#             if cliente and veiculo:
#                 data = {
#                     'nome_cliente': cliente.nome,
#                     'cpf': cliente.cpf,
#                     'email': cliente.email,
#                     'telefone': cliente.telefone,
#                     'endereco': cliente.endereco,
#                     'marca_veiculo': veiculo.marca,
#                     'modelo_veiculo': veiculo.modelo,
#                     'placa_veiculo': veiculo.placa,
#                     'ano_veiculo': veiculo.ano
#                 }
#                 return JsonResponse(data)
#             else:
#                 return JsonResponse({'error': 'Cliente não encontrado ou sem veículo.'}, status=400)
#         except Cliente.DoesNotExist:
#             return JsonResponse({'error': 'Cliente não encontrado.'}, status=400)
#
#
# def salvar_orcamento(request):
#     if request.method == 'POST':
#         nome_cliente = request.POST.get('nome_cliente')  # Ou onde você captura o nome do cliente
#         descricao_servicos = request.POST.get('descricao_servicos')
#         valor_estimado = request.POST.get('valor_estimado')
#
#         # Usar a função de busca para obter as informações do cliente e veículo
#         cliente_info = buscar_cliente_por_nome(request)  # Supondo que essa função retorna um dicionário com informações
#
#         cliente_obj = cliente_info.get('cliente_obj')  # Obtenha a instância do cliente da busca
#         veiculo_obj = cliente_info.get('veiculo_obj')  # Obtenha a instância do veículo associado
#
#         orcamento = OrcamentoNaoAprovado(
#             cliente=cliente_obj,
#             veiculo=veiculo_obj,
#             servicos_propostos=descricao_servicos,
#             valor_estimado=valor_estimado
#         )
#         orcamento.save()
#
#         # Redirecionar para uma página de sucesso ou para a página de detalhes do orçamento
#         return redirect('pagina_de_sucesso')  # Substitua 'pagina_de_sucesso' pela rota correta
#
#     return render(request, 'pagina_de_orcamento.html')