from django.forms import ModelForm
from .models import Funcionario

class FormFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome','sobrenome','cpf','tempo_de_servico','remuneracao']
