from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.receitas.fabrica import make_recipe
from .models import Receitas


def home(request):
    # receitas = Receitas.objects.filter(esta_publicado=True).order_by('-id')
    receitas = Receitas.objects.filter(
        esta_publicado=True,
    ).order_by('-id')

    return render(request, 'receitas/pages/home.html', context={
        'receitas': receitas,
    })
    # HTTP Response


def categoria(request, categoria_id):
    receitas = get_list_or_404(Receitas.objects.filter(
        categoria__id=categoria_id,
        esta_publicado=True,
    ).order_by('-id'))

    return render(request, 'receitas/pages/categoria.html', context={
        'receitas': receitas,
        'titulo': f'{receitas[0].categoria.nome} - Categoria | '
    })
    # HTTP Response


def receita(request, id):
    # receita = Receitas.objects.filter(
    #        pk=id,
    #        esta_publicado=True,
    #        ).order_by('-id').first()

    receita = get_object_or_404(Receitas, pk=id, esta_publicado=True)

    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': receita,
        'is_detail_page': True,
    })
    # HTTP Request


def pesquisa(request):
    return render(request, 'receitas/pages/pesquisa.html')
