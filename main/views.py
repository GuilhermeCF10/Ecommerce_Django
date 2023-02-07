from django.views.generic.edit import FormView
from main import forms
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormAdicionarProdutoAoCarrinho
from .models import Categoria, Produto
from .models import ItemPedido
from .forms import FormCriarPedido
from .carrinho import Carrinho
from django.views.decorators.http import require_POST


# ======================
#   Tela Fale conosco
# ======================
class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)
    

# ======================
#   Listar Produtos
# ======================
def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)

    if slug_categoria:
        categoria = get_object_or_404(Categoria,slug=slug_categoria)
        lista_produtos=Produto.objects.filter(categoria=categoria)

    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categorias,
        'lista_produtos': lista_produtos,
    }
    return render(request, 'produto/listar.html', contexto)



# ======================
#   Detalhes do Produtos
# ======================
def detalhes_produto(request, id, slug_produto):

    produto = get_object_or_404(Produto, id=id,slug=slug_produto,disponivel=True)
    form_adicionar_produto_ao_carrinho = FormAdicionarProdutoAoCarrinho()  # ----
    contexto = {
        'produto': produto,
        'form_produto_carrinho': form_adicionar_produto_ao_carrinho,  # ---
    }
    return render(request, 'produto/detalhes.html', contexto)



# ======================
#   Criar pedido
# ======================
def criar_pedido(request):
    
    carrinho = Carrinho(request)

    if request.method == 'POST':
        form = FormCriarPedido(request.POST)
        if form.is_valid():
            pedido = form.save()

            for item in carrinho:
                ItemPedido.objects.create(pedido=pedido, produto=item['produto'], preco=item['preco'], quantidade
                = item['quantidade'])
            carrinho.limpar_carrinho()
            return render(request, 'pedidos/pedido/concluir.html',{'pedido' : pedido})
    else:
        form = FormCriarPedido()
        return render(request, 'pedidos/pedido/criar.html', {'carrinho' : carrinho, 'form' : form})



# ============================
#   Adicionar ao carrinho
# ============================
@require_POST
def adicionar_ao_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    form = FormAdicionarProdutoAoCarrinho(request.POST)
    if form.is_valid():
        dados = form.cleaned_data
        carrinho.adicionar(produto=produto, quantidade=dados['quantidade'], atualizar_quantidade=dados['atualizar'])
    return redirect('detalhes_carrinho')


# ============================
#   Remover ao carrinho
# ============================
def remover_do_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    carrinho.remover(produto)
    return redirect('detalhes_carrinho')


# ============================
#   Detalhes ao carrinho
# ============================
def detalhes_carrinho(request):
    carrinho = Carrinho(request)
    for item in carrinho:
        item['formulario_adicionar_produto_ao_carrinho'] = FormAdicionarProdutoAoCarrinho(initial={'quantidade': item['quantidade'], 'atualizar': True})
    return render(request, 'carrinho/detalhes.html', {'carrinho': carrinho})