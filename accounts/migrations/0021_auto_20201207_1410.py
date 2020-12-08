# Generated by Django 3.1.3 on 2020-12-07 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20201207_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoDia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miércoles'), ('4', 'Jueves')], max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Catalogo día',
                'verbose_name_plural': 'Catalogo días',
            },
        ),
        migrations.CreateModel(
            name='CatalogoHora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TimeField(choices=[('0700', '07:00'), ('0730', '07:30'), ('0800', '08:00'), ('0830', '08:30'), ('0900', '09:00'), ('0930', '09:30')], max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Catalogo hora',
                'verbose_name_plural': 'Catalogo horas',
            },
        ),
        migrations.AlterField(
            model_name='asesor',
            name='subtetmas',
            field=models.ManyToManyField(through='accounts.TemarioAsesor', to='accounts.Subtema'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.catalogodia'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='hora',
            field=models.ForeignKey(choices=[('0700', '07:00'), ('0730', '07:30'), ('0800', '08:00'), ('0830', '08:30'), ('0900', '09:00'), ('0930', '09:30')], null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.catalogohora'),
        ),
        migrations.AlterField(
            model_name='asesor',
            name='horarios',
            field=models.ManyToManyField(through='accounts.Agenda', to='accounts.CatalogoDia'),
        ),
        migrations.DeleteModel(
            name='DiaAtencion',
        ),
        migrations.DeleteModel(
            name='Hora',
        ),
    ]
