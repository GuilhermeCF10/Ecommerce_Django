from django.contrib import admin
from .models import Categoria, Produto, Pedido, ItemPedido
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','slug','preco','estoque','disponivel','data_criacao','data_ultima_atualizacao']
    list_filter = ['disponivel', 'data_criacao','data_ultima_atualizacao']
    list_editable = ['preco', 'estoque', 'disponivel']
    prepopulated_fields = {'slug': ('nome',)}


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    raw_id_fields = ['produto']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'logradouro', 'numero',
    'complemento', 'bairro', 'cidade',
    'uf', 'cep', 'data_criacao', 'pago']
    list_filter = ['pago', 'data_criacao', 'nome']
    inlines = [ItemPedidoInline]