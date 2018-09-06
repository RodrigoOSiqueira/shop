# Generated by Django 2.1 on 2018-08-30 04:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_categoryshop_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_auto_20180828_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Compra Concluida'), (2, 'Compra Cancelada')], default=0, verbose_name='Situação')),
                ('payment_option', models.CharField(blank=True, choices=[('pagseguro', 'PagSeguro'), ('paypal', 'Paypal'), ('boleto', 'Boleto')], default='pagseguro', max_length=20, verbose_name='Opção de Pagamento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='OrderIten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('order', models.ForeignKey(on_delete='CASCADE', related_name='Itens', to='checkout.Order', verbose_name='Pedido')),
                ('product', models.ForeignKey(on_delete='CASCADE', to='shop.Product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do Pedido',
                'verbose_name_plural': 'Itens dos Pedidos',
            },
        ),
    ]
