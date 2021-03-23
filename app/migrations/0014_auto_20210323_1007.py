# Generated by Django 3.1.7 on 2021-03-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210323_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='customer',
            field=models.TextField(max_length=100, verbose_name='ФИО инициатора заявки'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='form',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер заказа-наряда'),
        ),
    ]
