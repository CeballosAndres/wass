# Generated by Django 3.1.3 on 2020-12-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20201212_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesor',
            name='subtetmas',
            field=models.ManyToManyField(through='accounts.TemarioAsesor', to='accounts.Subtema'),
        ),
    ]