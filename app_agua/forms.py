from django import forms
from .models import Pedido
class Solicitacao(forms.ModelForm):
    # qtd = forms.IntegerField(label = 'Quantidade',max_value=2,min_value=1)
    # data_entrega = forms.DateField(label = 'Data',widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    # predio = forms.CharField(label='Prédio', max_length=100)
    # sala = forms.CharField(label = 'Sala', max_length=11)
    class Meta:
        model = Pedido
        fields = ('id_usuario','id_sala','qtd','data')
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            #'qtd': forms.DateInput(attrs={'type': 'integer', 'max_value': 2, 'min_value': 1}),
            #'address': forms.Textarea(attrs={'cols': 10, 'rows': 3})
        }
        labels = {
            'id_usuario': 'Usuário',
            'id_sala': 'Sala',
            'qtd': 'Quantidade (máx. 2 unid.)'
        }