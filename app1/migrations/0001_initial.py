# Generated by Django 4.2.1 on 2023-05-23 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('subject_code', models.CharField(max_length=256)),
                ('day', models.CharField(max_length=256)),
                ('start_hour', models.CharField(max_length=256)),
                ('end_hour', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectsAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('subject_code', models.CharField(max_length=256)),
                ('semester', models.CharField(max_length=256)),
                ('sks', models.IntegerField()),
                ('day', models.CharField(max_length=256)),
                ('start_hour', models.IntegerField()),
                ('end_hour', models.IntegerField()),
                ('class_name', models.CharField(max_length=256)),
                ('lecturer', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UserSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
            ],
        ),
    ]
