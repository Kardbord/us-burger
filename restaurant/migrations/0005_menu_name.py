# Generated by Django 2.0.2 on 2018-02-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_menu_menu_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='Menu', max_length=200),
        ),
    ]