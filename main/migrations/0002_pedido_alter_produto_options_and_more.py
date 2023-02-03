# Generated by Django 4.1.6 on 2023-02-03 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('logradouro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=9)),
                ('data_criacao', models.DateField(auto_now=True)),
                ('pago', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-data_criacao',),
            },
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterIndexTogether(
            name='produto',
            index_together={('id', 'slug')},
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='main.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_pedido', to='main.produto')),
            ],
        ),
    ]
