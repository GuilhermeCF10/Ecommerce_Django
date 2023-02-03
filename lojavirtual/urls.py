"""lojavirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "main" 

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls,),
    
    # Index
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # Fale conosco
    path('fale-conosco/', views.ViewFaleConosco.as_view(),name="fale_conosco"),

    # Ajuda
    path('ajuda/', TemplateView.as_view(template_name='ajuda.html'), name='ajuda'),

    # Carrinho
    path('carrinho/', views.detalhes_carrinho, name='detalhes_carrinho'),
    path('carrinho/adicionar/<int:id_produto>/', views.adicionar_ao_carrinho,name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:id_produto>/', views.remover_do_carrinho,name='remover_do_carrinho'),

    # Pedidos
    path('pedidos/criar/', views.criar_pedido, name='criar_pedido'),

    # Produtos
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/<str:slug_categoria>/', views.listar_produtos, name='listar_produtos_por_categoria'),
    path('produto/ <int:id>/<str:slug_produto>', views.detalhes_produto, name='detalhes_produto'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
