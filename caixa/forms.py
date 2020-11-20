from django import forms
from estoque.models import Produto


class form_cadastrar_prooduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'