# Generated by Django 5.0.2 on 2024-03-05 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eusers',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='eusers',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='eusers',
            name='phone',
        ),
    ]
