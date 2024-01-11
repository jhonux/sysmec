from datetime import datetime

from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'tb_cliente'


class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=20)
    cor = models.CharField(max_length=20, default='desconhecida')
    km = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.modelo

    
    class Meta:
        db_table = 'tb_veiculo'

class OrcamentoNaoAprovado(models.Model):
    id = models.AutoField(primary_key=True)
    numero_orcamento = models.CharField(max_length=50, null=True)  # Número de orçamento gerado automaticamente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    servicos_propostos = models.TextField()
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    data_abertura = models.DateField(auto_now_add=True)
    data_proposta = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.numero_orcamento:
            self.numero_orcamento = self.generate_unique_number()
        super().save(*args, **kwargs)

    def generate_unique_number(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
        return timestamp

    def criar_ordem_servico_aberta(self):
        ordem_aberta = OrdemServicoAberta.objects.create(
            numero_ordem=self.numero_orcamento,  # Usando o número de orçamento como número de ordem
            data_ordem=self.data_abertura,  # Usando a data de aprovação do orçamento aprovado
            cliente=self.cliente,
            veiculo=self.veiculo,
            servico=self.servicos_propostos,
            valor_estimado=self.valor_estimado,
        )
        return ordem_aberta
    class Meta:
        db_table = 'tb_orcamentos_nao_aprovados'

class OrdemServicoAberta(models.Model):
    numero_ordem = models.CharField(max_length=20, primary_key=True, unique=True)
    data_ordem = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.numero_ordem:
            self.numero_ordem = self.generate_unique_number()
        super().save(*args, **kwargs)

    def transfer_to_concluida(self):
        ordem_concluida = OrdemServicoConcluida.objects.create(
            numero_ordem=self.numero_ordem,
            data_inicio=self.data_ordem,  # Usando a data de abertura como data de conclusão
            cliente=self.cliente,
            veiculo=self.veiculo,
            servico=self.servico,
            valor_total=self.valor_estimado,  # Usando o valor estimado como valor total
            data_conclusao_ordem=datetime.now().date()  # Defina a data de conclusão da ordem
        )

        return ordem_concluida
    # Restante da classe

    class Meta:
        db_table = 'tb_os_aberta'

class OrdemServicoConcluida(models.Model):
    numero_ordem = models.CharField(max_length=20, primary_key=True, unique=True)
    data_inicio = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_conclusao_ordem = models.DateField()

    class Meta:
        db_table = 'tb_os_concluida'




