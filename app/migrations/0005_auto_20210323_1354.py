# Generated by Django 3.1.7 on 2021-03-23 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210323_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.status', verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='tech',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tech', verbose_name='Сервисный инженер'),
        ),
    ]
