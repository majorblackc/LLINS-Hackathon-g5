# Generated by Django 3.2.3 on 2022-02-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budgeted', models.IntegerField()),
                ('issued', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('month', models.DateTimeField()),
                ('totalpatients', models.IntegerField()),
                ('patientswithnets', models.IntegerField()),
                ('patientswithoutnets', models.IntegerField()),
            ],
            options={
                'ordering': ['year'],
            },
        ),
    ]
