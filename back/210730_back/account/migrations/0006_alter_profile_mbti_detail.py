# Generated by Django 3.2.5 on 2021-07-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mbti_detail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
