# Generated by Django 4.2.3 on 2023-07-22 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_note'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
    ]
