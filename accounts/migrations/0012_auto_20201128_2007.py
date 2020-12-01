# Generated by Django 3.1.3 on 2020-11-29 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_tema'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='carreras',
            new_name='carrera',
        ),
        migrations.AddField(
            model_name='tema',
            name='materia',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='accounts.materia'),
        ),
    ]
