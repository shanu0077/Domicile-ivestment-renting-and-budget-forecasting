# Generated by Django 4.1.7 on 2023-05-12 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_appartment_bookings_delete_appartment_booking2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appartment_bookings',
            new_name='ab',
        ),
    ]
