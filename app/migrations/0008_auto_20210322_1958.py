# Generated by Django 3.1.7 on 2021-03-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210322_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='form',
            field=models.TextField(blank=True, default='', help_text='Номер заказа-наряда', max_length=10),
        ),
        migrations.AlterField(
            model_name='rec',
            name='result',
            field=models.TextField(blank=True, default='', help_text='Результат выезда', max_length=1000),
        ),
        migrations.AlterField(
            model_name='rec',
            name='sign',
            field=models.DateTimeField(blank=True, default='', help_text='Дата и время передачи заявки инженеру'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='staff',
            field=models.ForeignKey(default='', help_text='Диспетчер', on_delete=django.db.models.deletion.PROTECT, to='app.staff'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rec',
            name='status',
            field=models.ForeignKey(default=1, help_text='Статус заявки', on_delete=django.db.models.deletion.PROTECT, to='app.status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rec',
            name='store',
            field=models.ForeignKey(default=1, help_text='Торговая точка, адрес', on_delete=django.db.models.deletion.PROTECT, to='app.store'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rec',
            name='tech',
            field=models.ForeignKey(blank=True, default='', help_text='Сервисный инженер', on_delete=django.db.models.deletion.PROTECT, to='app.tech'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='trouble',
            field=models.ForeignKey(blank=True, default='', help_text='Категория неисправности', on_delete=django.db.models.deletion.PROTECT, to='app.trouble'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='visit',
            field=models.DateField(blank=True, default='', help_text='Дата визита инженера'),
        ),
    ]
