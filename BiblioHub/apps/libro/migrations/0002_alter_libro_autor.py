# Generated by Django 4.2 on 2023-05-16 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_alter_autor_nombre'),
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autor.autor', verbose_name='autor'),
        ),
    ]
