# Generated by Django 2.1 on 2018-08-16 21:22

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('blog', '0002_post_nreads'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryBlog',
        ),
    ]