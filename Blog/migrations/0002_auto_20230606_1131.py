# Generated by Django 3.1.13 on 2023-06-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Post',
            field=models.TextField(default='Ingresar Contenido:', max_length=2000, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Titulo',
            field=models.CharField(default='Titulo', max_length=100, unique=True, verbose_name='Titulo'),
        ),
    ]
