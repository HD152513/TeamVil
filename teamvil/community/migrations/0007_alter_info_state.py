# Generated by Django 3.2.5 on 2021-07-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_info_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
