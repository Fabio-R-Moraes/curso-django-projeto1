from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from .models import Receitas
from django.db.models import Q


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
    termo_procurado = request.GET.get('q', '').strip()

    if not termo_procurado:
        raise Http404()

    receitas = Receitas.objects.filter(
        Q(
            Q(titulo__icontains=termo_procurado) |
            Q(descricao__icontains=termo_procurado),
        ),
        esta_publicado=True,
    ).order_by('-titulo')

    return render(request, 'receitas/pages/pesquisa.html', {
        'page_title': f'Pesquisando por "{termo_procurado}" |',
        'receitas': receitas,
    })
