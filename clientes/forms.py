from django import forms
from django.forms import inlineformset_factory

from django.forms import ModelForm

from .models import Cliente, Veiculo, OrcamentoNaoAprovado


class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']

        # marca = forms.CharField(max_length=50)
        # modelo = forms.CharField(max_length=50)
        # ano = forms.CharField(max_length=50)
        # placa = forms.CharField(max_length=20)


# class VeiculoForms(forms.Form):
#     def __init__(self, *args, prefix=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         if prefix is not None:
#             self.fields[f'{prefix}-marca'] = forms.CharField(max_length=50)
#             self.fields[f'{prefix}-modelo'] = forms.CharField(max_length=50)
#             self.fields[f'{prefix}-ano'] = forms.CharField(max_length=50)
#             self.fields[f'{prefix}-placa'] = forms.CharField(max_length=20)

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'placa']

class CriarOrcamentoForm(forms.ModelForm):
    servicos_propostos = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))
    valor_estimado = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = OrcamentoNaoAprovado
        fields = ['servicos_propostos', 'valor_estimado']