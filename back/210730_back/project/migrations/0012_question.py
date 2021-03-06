# Generated by Django 3.2.5 on 2021-07-23 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('choice_cnt', models.IntegerField()),
                ('choice1', models.CharField(max_length=100)),
                ('choice2', models.CharField(max_length=100)),
                ('choice3', models.CharField(max_length=100, null=True)),
                ('choice4', models.CharField(max_length=100, null=True)),
                ('choice5', models.CharField(max_length=100, null=True)),
                ('project_id', models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
