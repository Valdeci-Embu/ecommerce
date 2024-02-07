"""Module that provides a python version of package import"""
from django.contrib import admin
from .models import Produto, Variacao
from .forms import VariacaoObrigatoria


class VariacaoInline(admin.TabularInline):
    model = Variacao
    formset = VariacaoObrigatoria
    min_num = 1
    extra = 0
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta',
                    'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
