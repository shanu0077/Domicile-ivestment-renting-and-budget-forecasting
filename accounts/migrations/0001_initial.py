# Generated by Django 4.1.4 on 2023-03-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_cab_driver', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_hotel_owner', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='firstname')),
                ('lastname', models.CharField(max_length=50, unique=True)),
                ('phone_num', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_normal_user', models.BooleanField(default=True)),
            ],
        ),
    ]
