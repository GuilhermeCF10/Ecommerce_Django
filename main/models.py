from django.db import models
from decimal import Decimal
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):

        return self.nome

    def get_absolute_url(self):
        return reverse('listar_produtos_por_categoria',args=[self.slug]) 

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria,related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='produtos/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        print(self)
        return reverse('detalhes_produto', args=[self.id ,self.slug])

class Meta:
    ordering = ('nome', )
    index_together = (('id', 'slug'),)
    def __str__(self):
        return self.nome

class Pedido(models.Model):

    # Dados do comprador:
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    # Dados específicos do pedido:
    data_criacao = models.DateField(auto_now=True)
    pago = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data_criacao',)

    def __str__(self):
        return 'Pedido #' + str(self.id)

    def get_total_geral(self):
        resultado = Decimal(0.0)
        for item in self.itens.all():
            subtotal = Decimal(item['quantidade'])*Decimal(item['preco'])
            resultado = resultado + subtotal
        return resultado


class ItemPedido(models.Model):

    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_pedido', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Pedido # ' + str(self.id)

    def get_subtotal(self):
        return self.preco * self.quantidade




# Create your models here.
# class Categoria(models.Model):
#     nome = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)

# class Meta:
#     ordering = ('nome',)
#     verbose_name = 'categoria'
#     verbose_name_plural = 'categorias'
    
#     def __str__(self):
#         return self.nome

# class Produto(models.Model):
#     categoria = models.ForeignKey(Categoria,related_name='produtos', on_delete=models.CASCADE)
#     nome = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     imagem = models.ImageField(upload_to='produtos/', blank=True)
#     descricao = models.TextField(blank=True)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     disponivel = models.BooleanField(default=True)
#     data_criacao = models.DateTimeField(auto_now_add=True)
#     data_atualizacao = models.DateTimeField(auto_now=True)

# class Meta:
#     ordering = ('nome',)
#     index_together = (('id', 'slug'),)
    
#     def __str__(self):
#         return self.nome







# from django.db import models

# class Categoria(models.Model):
#     slug = models.CharField(max_length=150, unique=True, db_index=True)
#     nome = models.CharField(max_length=150, db_index=True)
#     data_criacao = models.DateTimeField(auto_now_add=True)
#     data_ultima_atualizacao = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nome

# # class Produto(models.Model):
# #     nome = models.CharField(max_length=100, db_index=True)
# #     slug = models.SlugField(max_length=100, db_index=True)
# #     descricao = models.TextField(blank=True)
# #     preco = models.DecimalField(max_digits=10, decimal_places=2)
# #     disponivel = models.BooleanField(default=True)
# #     estoque = models.PositiveIntegerField()
# #     data_criacao = models.DateTimeField(auto_now_add=True)
# #     data_ultima_atualizacao = models.DateTimeField(auto_now=True)
# #     imagem = models.ImageField(upload_to='imagens-produtos', blank=True)

# #     def save(self, *args, **kwargs):
# #         print('O método save() foi chamado')
# #         print(f'Parâmetros: *args: {args}, **kwargs: {kwargs}')
# #         # Executa o método save() da classe ancestral, models.Model:
# #         super(Produto, self).save(*args, **kwargs)

# #     def __str__(self):
# #         return self.nome

# # Parte 2

# # TAMANHOS = (('P','Pequeno'),('M','Médio'),('G','Grande'))

# class Produto(models.Model):
#     slug = models.CharField(max_length=100, unique=True, db_index=True)
#     nome = models.CharField(max_length=100, db_index=True)
#     descricao = models.TextField(blank=True)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     categoria_id = models.ForeignKey(Categoria,null=True, on_delete=models.CASCADE)
#     disponivel = models.BooleanField(default=True)
#     estoque = models.PositiveIntegerField()
#     # tamanho = models.CharField(choices=TAMANHOS,max_length=1)
#     data_criacao = models.DateTimeField(auto_now_add=True)
#     data_ultima_atualizacao = models.DateTimeField(auto_now = True)

#     imagem = models.ImageField(upload_to='imagens-produtos', blank=True)

#     def __str__(self):
#         return self.nome

# class Loja(models.Model):
#     nome = models.CharField(max_length=50)
#     endereco = models.CharField(max_length=50)
#     cidade = models.CharField(max_length=30)
#     uf = models.CharField(max_length=2)
#     cep = models.CharField(max_length=8)
#     email = models.EmailField()
#     produtos = models.ManyToManyField(Produto,blank=True)



# class Endereco(models.Model):
#     logradouro = models.CharField(max_length=50)
#     numero = models.CharField(max_length=10)
#     bairro = models.CharField(max_length=20)
#     cidade = models.CharField(max_length=30)
#     uf = models.CharField(max_length=2)
#     cep = models.CharField(max_length=8)

# class Cliente(models.Model):
#     nome = models.CharField(max_length=50)
#     endereco = models.CharField(max_length=100)
#     # Outros atributos aqui...
#     endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE,primary_key=True)


# class Funcionario(models.Model):
#     # outros atributos do funcionário aqui...
#     gerente = models.ForeignKey('self',on_delete = models.PROTECT)
    

# class Conta(models.Model):
#     # Classe utilizada em uma aplicação contábil
#     # para representar um plano de contas
#     descricao = models.CharField(max_length = 100)
#     saldo = models.FloatField()
#     superior = models.ForeignKey('self',on_delete = models.PROTECT) # Conta superior