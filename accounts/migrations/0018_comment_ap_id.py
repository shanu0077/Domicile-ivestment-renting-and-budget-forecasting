# Generated by Django 4.1.7 on 2023-05-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ap_id',
            field=models.IntegerField(null=True),
        ),
    ]
