from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='receitas-home'),
    path('receitas/categoria/<int:categoria_id>/',
         views.categoria,
         name='categoria'),
    path('receitas/<int:id>/', views.receita, name='receitas-receita'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
