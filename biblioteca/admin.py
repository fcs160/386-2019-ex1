from django.contrib import admin
from .models import *


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome')


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'data_nascimento', 'email')


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao')


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data_retirado', 'data_devolucao', 'devolvido')
    filter_horizontal = ['livro']


admin.site.register(Autor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Livro)
admin.site.register(Emprestimo, EmprestimoAdmin)

# Register your models here.
