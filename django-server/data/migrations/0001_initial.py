# Generated by Django 3.2 on 2024-01-29 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('additional_info', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=10, unique=True)),
                ('stock_name', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('sell', 'Sell Stock'), ('buy', 'Buy Stock')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_price', models.DecimalField(decimal_places=15, max_digits=20)),
                ('closing_price', models.DecimalField(decimal_places=15, max_digits=20)),
                ('high', models.DecimalField(decimal_places=15, max_digits=20)),
                ('low', models.DecimalField(decimal_places=15, max_digits=20)),
                ('volume', models.BigIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.stock')),
            ],
        ),
    ]
