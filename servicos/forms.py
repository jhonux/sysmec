# from django import forms
# from .models import OrcamentoNaoAprovado, Cliente
#
#
# # class NovoOrcamentoForm(forms.Form):
# #     nome_cliente = forms.CharField(label='Nome do Cliente', max_length=100, required=False)
# #     marca_veiculo = forms.CharField(label='Marca do Veículo', max_length=50, required=False)
# #     modelo_veiculo = forms.CharField(label='Modelo do Veículo', max_length=50, required=False)
# #     ano_veiculo = forms.CharField(label='Ano do Veículo', max_length=4, required=False)
# #     placa_veiculo = forms.CharField(label='Placa do Veículo', max_length=20, required=False)
# #
# #     def buscar_cliente(self):
# #         nome_cliente = self.cleaned_data['nome_cliente']
# #         try:
# #             cliente = Cliente.objects.get(nome=nome_cliente)
# #             return cliente
# #         except Cliente.DoesNotExist:
# #             return None
# # #
# class NovoOrcamentoForm(forms.ModelForm):
#     cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Cliente')
#
#     class Meta:
#         model = OrcamentoNaoAprovado
#         fields = ['cliente', 'servicos_propostos', 'valor_estimado']
#
#     cpf = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['cliente'].widget.attrs.update({'onchange': 'update_fields(this);'})
#
#         # Outros campos e personalizações do formulário
#
