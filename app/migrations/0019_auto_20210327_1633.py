# Generated by Django 3.1.7 on 2021-03-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210327_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='visit_day_begin',
            field=models.DateField(null=True, verbose_name='Дата начала работ'),
        ),
        migrations.AlterField(
            model_name='rec',
            name='visit_time_begin',
            field=models.TimeField(null=True, verbose_name='Время начала работ'),
        ),
    ]
