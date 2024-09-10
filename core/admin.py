from django.contrib import admin

from .models import Produtos, Clientes

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')

admin.site.register(Produtos,ProdutoAdmin)
admin.site.register(Clientes, ClientesAdmin)
