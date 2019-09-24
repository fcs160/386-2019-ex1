from django.contrib import admin
from .models import *


class ContatoAdmin(admin.ModelAdmin):
   list_display = ('nome','email','endereco','data_nascimento','telefone')

admin.site.register(Contato, ContatoAdmin)

class LivroAdmin (admin.ModelAdmin):
   list_display = ('Titulo','Nome_autor','Assunto','Editora','ISBN','Ano_publicacao')

admin.site.register(Livro, LivroAdmin)

class CompraAdmin(admin.ModelAdmin):
   list_display = ('nomec','descricaoProduto','qtdPrevistoMes','precoMax')

admin.site.register(Compra, CompraAdmin)

class DespesaAdmin(admin.ModelAdmin):
   list_display = ('datacriacao','tipodespesa','descricao','formapagamento','vencimento','quitado')

admin.site.register(Despesa, DespesaAdmin)
# Register your models here.
