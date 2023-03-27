from django.shortcuts import render
from django.http import HttpResponse

#HTTP Request
def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'nome':'Fábio Rodrigues de Moraes',
    })
    #HTTP Response


