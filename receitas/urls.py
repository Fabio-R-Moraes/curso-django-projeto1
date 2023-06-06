from django.urls import path
from receitas import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'receitas'

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/pesquisa/', views.pesquisa, name='pesquisa'),
    path('receitas/categoria/<int:categoria_id>/',
         views.categoria,
         name='categoria'),
    path('receitas/<int:id>/', views.receita, name='receita'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
