# Generated by Django 3.2.5 on 2021-07-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210701_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
