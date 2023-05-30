from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHomepage(forms.Form):  # form.Form é um formulario padrão do django
    email = forms.EmailField(label=False)


# para criação de uruario utilizando o django, as 04 linhas abaixo são padrões
class CriarContaForm(UserCreationForm):  # UserCreationForm formulario personalizado do django
    email = forms.EmailField()   # para tornar o campo obrigatorio -> (required=False)


    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')
