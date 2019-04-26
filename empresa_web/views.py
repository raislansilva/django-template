from django.shortcuts import render
from .models import Funcionario
from .form import FormFuncionario
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def home(request):
    data = {}
    return render(request,"views/home.html", data)


def show(request):
    data = {}
    data['funcionarios'] = Funcionario.objects.all()
    return render(request, 'views/show.html', data)



def create(request):
    data ={}
    form = FormFuncionario(request.POST or None)
    if form.is_valid():
        form.save()
        #request.session['msg'] = 'Usuario Cadastrado'
        messages.success(request,'Usuario Cadastrado')
    data['form'] = form
    return render(request, 'views/form.html', data)


def update(request, pk):
    data = {}
    transacao = Funcionario.objects.get(pk=pk)
    form = FormFuncionario(request.POST or None, instance = transacao)
    if form.is_valid():
        form.save()
        return redirect('url_show')
    data['form'] = form
    data['funcionarios'] = transacao
    return render(request, 'views/form.html', data)


def pageDelete(request, pk):
    data = {}
    transacao = Funcionario.objects.get(pk=pk)
    data['funcionario'] = transacao
    return render(request, 'views/delete.html', data)


def delete(request, pk):
    transacao = Funcionario.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_show')

def pagelogin(request):
    return render(request, 'views/login.html')




