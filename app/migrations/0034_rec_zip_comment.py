# Generated by Django 3.1.7 on 2021-03-31 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20210330_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='rec',
            name='zip_comment',
            field=models.TextField(max_length=1000, null=True, verbose_name='Комментарий ЗИП'),
        ),
    ]