# Generated by Django 3.2.5 on 2021-07-13 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Com',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('write_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('view_cnt', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.IntegerField()),
                ('content', models.TextField()),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('write_date', models.DateTimeField(auto_now_add=True)),
                ('com_id', models.ForeignKey(db_column='com_id', on_delete=django.db.models.deletion.CASCADE, to='community.com')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
