# Generated by Django 3.1.5 on 2022-06-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location1', models.CharField(choices=[('Corporate Headoffice', 'CH'), ('Operations Department', 'OD'), ('Work Station', 'WS'), ('Marketing Division', 'MD')], max_length=50)),
                ('location2', models.TextField()),
                ('decription', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('severity', models.CharField(choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'), ('Fatal', 'Fatal')], max_length=20)),
                ('cause', models.TextField()),
                ('actions', models.TextField()),
                ('type_env', models.BooleanField()),
                ('type_inju', models.BooleanField()),
                ('type_property', models.BooleanField()),
                ('type_vehicle', models.BooleanField()),
                ('submitted', models.BooleanField()),
                ('reported_by_id', models.IntegerField()),
            ],
        ),
    ]
