from django.contrib import admin
from .models import Pessoa, Contato


@admin.action(description='Ativar todas as pessoas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.action(description='Desativar todas as pessoas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)


class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nasc',
        'ativa'
    ]

    list_filter = [
        'ativa',
        'data_nasc']

    search_fields = [
        'nome_completo'
    ]
    actions = [
        ativar_todos
    ]


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)