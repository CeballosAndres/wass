# Generated by Django 3.1.3 on 2020-11-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_asesor_horarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='clave_materia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='materia',
            name='competencia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
