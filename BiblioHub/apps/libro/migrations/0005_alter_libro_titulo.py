# Generated by Django 4.2 on 2023-05-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_alter_libro_autor_alter_libro_borrado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.TextField(max_length=200, verbose_name='Nombre'),
        ),
    ]
