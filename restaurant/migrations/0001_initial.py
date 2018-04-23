# Generated by Django 2.0.2 on 2018-04-22 03:25

from django.db import migrations, models
import django.db.models.deletion
import utility.create_random_string


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pin', models.CharField(default=utility.create_random_string.create_random_string, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Menu', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(verbose_name=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(default=0, max_length=4)),
                ('email', models.EmailField(default='customer@www.com', max_length=254)),
                ('name', models.CharField(default='Customer Smith', max_length=254)),
                ('order_items_are_available', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('cooking', models.BooleanField(default=False)),
                ('cooked', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('comment', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.MenuItem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Order')),
            ],
        ),
        migrations.CreateModel(
            name='SupplyAmt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='SupplyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('units', models.CharField(max_length=10)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaitTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wait_time', models.CharField(default='0', max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='supplyamt',
            name='supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.SupplyItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurant.Table'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_items',
            field=models.ManyToManyField(to='restaurant.MenuItem'),
        ),
    ]
