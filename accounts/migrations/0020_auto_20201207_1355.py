# Generated by Django 3.1.3 on 2020-12-07 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20201202_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TimeField(unique=True)),
            ],
            options={
                'verbose_name': 'Hora',
                'verbose_name_plural': 'Horas',
            },
        ),
        migrations.AlterField(
            model_name='asesor',
            name='subtetmas',
            field=models.ManyToManyField(through='accounts.TemarioAsesor', to='accounts.Subtema'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.hora'),
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('asesor', 'dia', 'hora')},
        ),
        migrations.DeleteModel(
            name='HorarioAtencion',
        ),
    ]
