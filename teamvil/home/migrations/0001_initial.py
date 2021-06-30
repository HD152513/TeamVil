# Generated by Django 3.2.4 on 2021-06-30 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Field1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Region1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region1', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Region2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region2', models.CharField(max_length=20)),
                ('region1_id', models.ForeignKey(db_column='region1_id', on_delete=django.db.models.deletion.CASCADE, to='home.region1')),
            ],
        ),
    ]
