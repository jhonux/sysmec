# Generated by Django 4.2.4 on 2023-08-18 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_veiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='data_nascimento',
        ),
    ]
