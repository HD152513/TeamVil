# Generated by Django 3.2.5 on 2021-07-23 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_term_term_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_review',
            name='question1',
        ),
    ]
