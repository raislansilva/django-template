from django.shortcuts import render
from .models import Funcionario
from .form import FormFuncionario
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your crud here.

@login_required
def home(request):
    data = {}
    return render(request,"crud/home.html", data)

@login_required
def show(request):
    data = {}
    data['funcionarios'] = Funcionario.objects.all()
    return render(request, 'crud/show.html', data)


@login_required
def create(request):
    data ={}
    form = FormFuncionario(request.POST or None)
    if form.is_valid():
        form.save()
        #request.session['msg'] = 'Usuario Cadastrado'
        messages.success(request,'Usuario Cadastrado')
    data['form'] = form
    return render(request, 'crud/form.html', data)

@login_required
def update(request, pk):
    data = {}
    transacao = Funcionario.objects.get(pk=pk)
    form = FormFuncionario(request.POST or None, instance = transacao)
    if form.is_valid():
        form.save()
        return redirect('url_show')
    data['form'] = form
    data['funcionarios'] = transacao
    return render(request, 'crud/form.html', data)

@login_required
def pageDelete(request, pk):
    data = {}
    transacao = Funcionario.objects.get(pk=pk)
    data['funcionario'] = transacao
    return render(request, 'crud/delete.html', data)

@login_required
def delete(request, pk):
    transacao = Funcionario.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_show')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




