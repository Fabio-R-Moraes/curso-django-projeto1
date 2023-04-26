from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='receitas-home'),
    path('receitas/<int:id>/', views.receita, name='receitas-receita'),
]
