# Generated by Django 3.1.3 on 2020-11-29 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201128_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materia',
            options={'verbose_name': 'Materia', 'verbose_name_plural': 'Materias'},
        ),
        migrations.AddField(
            model_name='materia',
            name='carreras',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='accounts.carrera'),
        ),
    ]
