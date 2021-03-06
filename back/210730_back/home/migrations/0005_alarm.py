# Generated by Django 3.2.5 on 2021-07-25 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0024_question_isrequired'),
        ('home', '0004_alter_like_to_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('content', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=200)),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_date', models.DateTimeField(null=True)),
                ('check', models.IntegerField(default=0)),
                ('like_id', models.ForeignKey(db_column='like_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.like')),
                ('member_id', models.ForeignKey(db_column='member_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='project.member')),
                ('scrap_id', models.ForeignKey(db_column='scrap_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.scrap')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
