# Generated by Django 4.2.6 on 2023-10-27 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(max_length=10)),
                ('area_name', models.CharField(max_length=100)),
                ('coordinates', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('anonymity_status', models.BooleanField()),
                ('crime_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.crimetype')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.location')),
            ],
        ),
    ]
