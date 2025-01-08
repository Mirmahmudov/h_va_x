# Generated by Django 5.1.4 on 2025-01-06 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Incorrect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('correct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.correct')),
            ],
        ),
    ]
