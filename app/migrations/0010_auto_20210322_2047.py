# Generated by Django 3.1.7 on 2021-03-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210322_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='sign',
            field=models.DateTimeField(blank=True, help_text='Дата и время передачи заявки инженеру', null=True),
        ),
        migrations.AlterField(
            model_name='rec',
            name='visit',
            field=models.DateField(blank=True, help_text='Дата визита инженера', null=True),
        ),
    ]
