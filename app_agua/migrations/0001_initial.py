# Generated by Django 4.2.6 on 2023-10-27 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_campus', models.CharField(max_length=100, verbose_name='Campus')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campus',
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_colaborador', models.CharField(max_length=100, verbose_name='Nome colaborador')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_predio', models.CharField(max_length=100, verbose_name='Nome prédio')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agua.campus')),
            ],
            options={
                'verbose_name': 'Predio',
                'verbose_name_plural': 'Predios',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_sala', models.CharField(max_length=100, verbose_name='Nome sala')),
                ('tipo_ambiente', models.CharField(choices=[('Sala de Aula', 'Sala de Aula'), ('Laboratório', 'Laboratório'), ('Banheiro', 'Banheiro')], max_length=100, verbose_name='Tipo de Ambiente')),
                ('criado_sala', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado_sala', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('predio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agua.predio')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=100, verbose_name='Nome usuário')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('id_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agua.sala')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField(verbose_name='Quantidade')),
                ('data', models.DateField(verbose_name='Data de Entrega')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('id_colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agua.colaborador')),
                ('id_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agua.sala')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_agua.usuario')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
