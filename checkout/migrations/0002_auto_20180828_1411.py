# Generated by Django 2.1 on 2018-08-28 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_categoryshop_description'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartiten',
            unique_together={('cart_id', 'product')},
        ),
    ]
