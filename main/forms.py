from django import forms
from django.core.mail import send_mail
from lojavirtual import settings
from .models import Pedido

class FormFaleConosco(forms.Form):
    nome = forms.CharField(required=True, initial='Seu nome aqui')
    email_origem = forms.EmailField(label = 'Entre com seu e-mail.',initial='seu e-mail aqui')
    mensagem = forms.CharField(required=True, widget=forms.Textarea)
    
    def enviar_mensagem_por_email(self):
        send_mail('FALE CONOSCO: Mensagem recebida.',self.data['mensagem'],self.data['email_origem'],[settings.EMAIL_FALE_CONOSCO],fail_silently=False)

    # se quiser realmente enviar o email só seguir o passo a passo da pag 368


OPCOES_QUANTIDADE_PRODUTO = []

for i in range(1,50):
    OPCOES_QUANTIDADE_PRODUTO.append((i, str(i)))

class FormAdicionarProdutoAoCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField(choices=OPCOES_QUANTIDADE_PRODUTO, coerce=int)
    atualizar = forms.BooleanField(required=False,widget=forms.HiddenInput)


class FormCriarPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep']