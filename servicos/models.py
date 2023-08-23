# from django.db import models
# from clientes.models import Cliente, Veiculo
# from datetime import datetime
# import random
#
# class OrcamentoNaoAprovado(models.Model):
#     id = models.AutoField(primary_key=True)
#     numero_orcamento = models.CharField(max_length=20, null=True)  # Número de orçamento gerado automaticamente
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
#     servicos_propostos = models.TextField()
#     valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
#     data_abertura = models.DateField(auto_now_add=True)
#     data_proposta = models.DateField(auto_now_add=True)
#
#     def save(self, *args, **kwargs):
#         if not self.numero_orcamento:
#             self.numero_orcamento = self.generate_unique_number()
#         super().save(*args, **kwargs)
#
#     def generate_unique_number(self):
#         timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
#         return f'ORC-{timestamp}'
#
#     class Meta:
#         db_table = 'tb_orcamentos_nao_aprovados'
#
#
# class OrcamentoAprovado(models.Model):
#     id = models.AutoField(primary_key=True)
#     numero_orcamento = models.CharField(max_length=20, default='')  # Mesmo número de orçamento
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
#     servicos_propostos = models.TextField()
#     valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
#     data_abertura = models.DateField(auto_now_add=True)
#     data_aprovacao = models.DateField()
#
#     def criar_ordem_servico_aberta(self):
#         ordem_aberta = OrdemServicoAberta.objects.create(
#             numero_ordem=self.numero_orcamento,  # Usando o número de orçamento como número de ordem
#             data_ordem=self.data_aprovacao,  # Usando a data de aprovação do orçamento aprovado
#             cliente=self.cliente,
#             veiculo=self.veiculo,
#             servico=self.servicos_propostos,
#             valor_estimado=self.valor_estimado,
#         )
#         return ordem_aberta
#
#     class Meta:
#         db_table = 'tb_orcamentos_aprovados'
#
#
# class OrdemServicoAberta(models.Model):
#     numero_ordem = models.CharField(max_length=20, primary_key=True, unique=True)
#     data_ordem = models.DateField()
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
#     servico = models.CharField(max_length=100)
#     valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
#
#     def save(self, *args, **kwargs):
#         if not self.numero_ordem:
#             self.numero_ordem = self.generate_unique_number()
#         super().save(*args, **kwargs)
#
#     # Restante da classe
#
#     class Meta:
#         db_table = 'tb_os_aberta'
#
# class OrdemServicoConcluida(models.Model):
#     numero_ordem = models.CharField(max_length=20, primary_key=True, unique=True)
#     data_conclusao = models.DateField()
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
#     servico = models.CharField(max_length=100)
#     valor_total = models.DecimalField(max_digits=10, decimal_places=2)
#     data_conclusao_ordem = models.DateField()
#
#     @classmethod
#     def transfer(cls, ordem_aberta):
#         ordem_concluida = cls.objects.create(
#             numero_ordem=ordem_aberta.numero_ordem,
#             data_conclusao=ordem_aberta.data_ordem,  # Usando a data de abertura como data de conclusão
#             cliente=ordem_aberta.cliente,
#             veiculo=ordem_aberta.veiculo,
#             servico=ordem_aberta.servico,
#             valor_total=ordem_aberta.valor_estimado,  # Usando o valor estimado como valor total
#             data_conclusao_ordem=datetime.now().date()  # Defina a data de conclusão da ordem
#         )
#         ordem_aberta.delete()  # Remover a ordem de serviço em aberto
#         return ordem_concluida
#
#     class Meta:
#         db_table = 'tb_os_concluida'
