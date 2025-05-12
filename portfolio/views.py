from django.shortcuts import render
from .dados import habilidades, projetos


def home(request):
    contexto = {
        'habilidades':habilidades,
        'projetos':projetos
    }
    return render(request, 'home.html', contexto)
    

def lista_projetos(request):
    return render(request, 'home.html', {'projetos':projetos})

def detalhes_projeto(request, id_projeto):
    projeto = projetos.get(id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto':projeto})
