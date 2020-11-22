# Generated by Django 3.1.3 on 2020-11-22 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20201113_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jefe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=200, null=True)),
                ('clave_empleado', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('usuario', models.OneToOneField(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('jefe', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.jefe')),
            ],
        ),
        migrations.CreateModel(
            name='Asesorado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('usuario', models.OneToOneField(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=200, null=True)),
                ('clave_empleado', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('departamento', models.ForeignKey(null=True,
                                                   on_delete=django.db.models.deletion.SET_NULL,
                                                   to='accounts.departamento')),
                ('usuario', models.OneToOneField(null=True,
                                                 on_delete=django.db.models.deletion.CASCADE,
                                                 to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carrera',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='accounts.departamento'),
        ),
    ]
