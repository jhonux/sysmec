# Generated by Django 4.2.4 on 2023-08-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_orcamentonaoaprovado_orcamentoaprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamentoaprovado',
            name='numero_orcamento',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orcamentonaoaprovado',
            name='numero_orcamento',
            field=models.CharField(max_length=20, null=True),
        ),
    ]