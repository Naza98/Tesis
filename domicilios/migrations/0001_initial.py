# Generated by Django 2.2.13 on 2021-06-14 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_barrio', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Barrio',
                'verbose_name_plural': 'Barrios',
                'db_table': 'Barrios',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_provincia', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_localidad', models.CharField(max_length=300)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domicilios.Provincia')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'db_table': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(blank=True, max_length=300, null=True)),
                ('altura', models.CharField(blank=True, max_length=300, null=True)),
                ('manzana', models.CharField(blank=True, max_length=300, null=True)),
                ('departamento', models.CharField(blank=True, max_length=300, null=True)),
                ('piso', models.CharField(blank=True, max_length=300, null=True)),
                ('observacion', models.CharField(blank=True, max_length=600, null=True)),
                ('baja', models.BooleanField(default=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('barrio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domicilios.Barrio')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.Cliente')),
            ],
            options={
                'db_table': 'Domicilios',
            },
        ),
        migrations.AddField(
            model_name='barrio',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domicilios.Localidad'),
        ),
    ]
