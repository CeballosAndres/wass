# Generated by Django 3.1.3 on 2020-11-24 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_asesorado_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesor',
            name='nombre',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='departamento',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    to='accounts.departamento'),
        ),
    ]
