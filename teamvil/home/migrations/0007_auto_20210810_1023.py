# Generated by Django 3.2.5 on 2021-08-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_alarm_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='url',
        ),
        migrations.AddField(
            model_name='alarm',
            name='member_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alarm',
            name='project_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
