# Generated by Django 4.2.2 on 2023-06-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20230608_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Post',
            field=models.TextField(default='Ingresar Contenido:', max_length=8000, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Titulo',
            field=models.CharField(default='Titulo', max_length=150, unique=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='registro_usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='registro_usuario',
            name='mail',
            field=models.EmailField(max_length=40),
        ),
    ]
