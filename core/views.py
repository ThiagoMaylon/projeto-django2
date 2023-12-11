from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto
from django.contrib import messages

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def produto(request):
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto Salvo com sucesso')
                form = ProdutoModelForm()
                
            else:
                messages.error(request, 'Erro ao salvar o Produto')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

def contato(request):
    forms = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if forms.is_valid():
            forms.send_email()
            messages.success(request, 'E-mail enviado com sucesso')
            forms = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
        
    context = {
        'form': forms
    }
    return render(request, 'contato.html', context)



