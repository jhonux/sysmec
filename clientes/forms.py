from django import forms
from django.forms import inlineformset_factory
from .models import Cliente, Veiculo, OrcamentoNaoAprovado


class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'marca', 'placa', 'ano', 'cor', 'km']



class CriarOrcamentoForm(forms.ModelForm):

    servicos_propostos = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))
    valor_estimado = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = OrcamentoNaoAprovado
        fields = ['servicos_propostos', 'valor_estimado']