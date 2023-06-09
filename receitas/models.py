from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome


class Receitas(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    tempo_preparo = models.IntegerField()
    unidade_tempo_preparo = models.CharField(max_length=65)
    porcoes = models.IntegerField()
    unidade_porcoes = models.CharField(max_length=65)
    modo_preparo = models.TextField()
    modo_preparo_html = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    esta_publicado = models.BooleanField(default=False)
    receita_imagem = models.ImageField(upload_to='receitas/receitas_imagens/%d/%m/%Y/',
                                       blank=True, default=''
                                       )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.titulo
