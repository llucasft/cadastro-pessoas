from django import forms
from django.forms import fields, models
from .models import Pessoa, Contato


class PessoaForm(forms.ModelForm):
    data_nasc = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nasc', 'ativa']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']