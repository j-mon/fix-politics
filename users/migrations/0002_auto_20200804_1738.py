# Generated by Django 3.0.8 on 2020-08-04 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='areas',
            new_name='prof_impacts',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='loc',
            new_name='prof_location',
        ),
    ]
