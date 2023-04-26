from django.shortcuts import render
from django.http import HttpResponse
from utils.receitas.fabrica import make_recipe

#HTTP Request
def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'receitas':[make_recipe() for _ in range(10)],
    })
    #HTTP Response

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita':make_recipe(),
        'is_detail_page':True,
    })
