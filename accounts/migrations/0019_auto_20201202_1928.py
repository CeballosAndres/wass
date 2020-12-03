# Generated by Django 3.1.3 on 2020-12-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20201201_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesor',
            name='subtetmas',
            field=models.ManyToManyField(through='accounts.TemarioAsesor', to='accounts.Subtema'),
        ),
        migrations.AlterField(
            model_name='temarioasesor',
            name='activo',
            field=models.BooleanField(default=False, verbose_name='Activo/no activo'),
        ),
    ]
