# Generated by Django 3.1.7 on 2021-03-24 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210324_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rec',
            options={'ordering': ['-rec_time'], 'permissions': (('can_add_and_update', 'Может rec_list, rec_detail, rec_create и rec_update'), ('can_see_rec_list', 'Может только rec_list и rec_detail'))},
        ),
    ]
