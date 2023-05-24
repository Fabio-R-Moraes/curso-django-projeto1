from django.contrib import admin
from .models import Categoria, Receitas


class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Receitas)
class ReceitasAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)
