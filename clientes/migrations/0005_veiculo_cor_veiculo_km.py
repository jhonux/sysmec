# Generated by Django 4.2.4 on 2023-08-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_remove_cliente_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(default='desconhecida', max_length=20),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='km',
            field=models.IntegerField(default=0),
        ),
    ]
