# Generated by Django 2.2.6 on 2019-11-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_auto_20191112_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_de_execucao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data de execução'),
        ),
    ]
