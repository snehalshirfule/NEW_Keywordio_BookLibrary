# Generated by Django 3.2.7 on 2021-11-11 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='admin',
            new_name='lms_admin',
        ),
        migrations.AlterModelTable(
            name='lms_admin',
            table='lms_admin',
        ),
    ]