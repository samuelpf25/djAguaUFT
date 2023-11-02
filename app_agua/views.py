from django.shortcuts import render
from .forms import Solicitacao
from django.contrib import messages

from .models import Pedido


def index(request):
    context = {
    'curso': 'Programação Web com Django Framework',
    'outro': 'Django é massa'
    }
    return render(request,'index.html', context)

def form_solicitacao(request):
    form = Solicitacao(request.POST or None)
    if str(request.method == 'POST'):
        if form.is_valid():
            #pedido = Pedido.objects.get(pk=1)
            form = Solicitacao(request.POST) #, instance=pedido
            form.save()
            messages.success(request, 'Solicitação registrada com sucesso!')
        else:
            messages.error(request, 'Erro ao salvar dados!')
    contexto ={
    'form': form
    }
    return render(request,'form_solicitacao.html', contexto)