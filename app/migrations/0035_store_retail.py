# Generated by Django 3.1.7 on 2021-04-03 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_rec_zip_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='retail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.retail', verbose_name='Торговая сеть'),
        ),
    ]
