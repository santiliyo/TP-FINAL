# Generated by Django 4.2.2 on 2023-06-11 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_alter_categoria_id_alter_post_post_alter_post_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.registro_usuario'),
        ),
    ]