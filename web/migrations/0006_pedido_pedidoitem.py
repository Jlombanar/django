# Generated by Django 5.1.4 on 2025-02-25 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_carrito_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.pedido')),
            ],
        ),
    ]
