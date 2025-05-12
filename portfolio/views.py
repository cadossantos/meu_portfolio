from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render

from .dados import habilidades, projetos
from .forms import ContatoForm

def home(request):
    form = ContatoForm()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            assunto = f'Nova mensagem de contato do portfólio - {nome}'

            corpo_email = f'Nome: {nome}\nE-mail: {email}\nMensagem:\n{mensagem}'

            send_mail(
                assunto,
                corpo_email,
                email, # remetente
                ['cadossantos@proton.me'], # destino
                fail_silently=False
            )
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
    
    contexto = {
        'habilidades':habilidades,
        'projetos':projetos,
        'form':form
    }
    return render(request, 'home.html', contexto)    

def lista_projetos(request):
    return render(request, 'home.html', {'projetos':projetos})

def detalhes_projeto(request, id_projeto):
    projeto = projetos.get(id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto':projeto})
