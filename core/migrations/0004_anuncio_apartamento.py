# Generated by Django 2.2.5 on 2019-10-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_compra_despesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=30)),
                ('textoTitulo', models.CharField(max_length=30)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('textoAnuncio', models.CharField(max_length=200)),
                ('nomeContato', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=15)),
                ('secao', models.CharField(max_length=30)),
                ('tipoAnuncio', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('qtdQuartos', models.PositiveIntegerField()),
                ('proprietario', models.CharField(max_length=30)),
                ('valorCondominio', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]