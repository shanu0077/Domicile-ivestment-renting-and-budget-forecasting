# Generated by Django 4.1.7 on 2023-05-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_appartment_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=50)),
                ('appartment_name', models.CharField(default='', max_length=50)),
                ('cmt', models.CharField(default='', max_length=250)),
            ],
        ),
    ]