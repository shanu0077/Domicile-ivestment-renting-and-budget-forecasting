# Generated by Django 4.1.4 on 2023-03-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_password_hotelowner_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelowner',
            old_name='name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='hotelowner',
            name='hotel_name',
            field=models.CharField(default=0, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelowner',
            name='password',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotelowner',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
