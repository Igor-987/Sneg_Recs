# Generated by Django 3.1.7 on 2021-03-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210323_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='rec',
            name='jpg',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Скан-копия заказа-наряда'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='form',
            field=models.CharField(max_length=10, null=True, verbose_name='Номер заказа-наряда'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='result',
            field=models.TextField(max_length=1000, null=True, verbose_name='Результат выезда'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='sign',
            field=models.DateTimeField(null=True, verbose_name='Дата и время передачи заявки инженеру'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='tech',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tech', verbose_name='Сервисный инженер'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='trouble',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trouble', verbose_name='Категория неисправности'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='visit',
            field=models.DateField(null=True, verbose_name='Дата визита инженера'),
        ),
    ]
