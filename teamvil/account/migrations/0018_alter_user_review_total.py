# Generated by Django 3.2.5 on 2021-08-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_message_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_review',
            name='total',
            field=models.IntegerField(),
        ),
    ]
