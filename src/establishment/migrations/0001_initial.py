# Generated by Django 4.2 on 2024-03-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('locations', models.CharField(max_length=100)),
                ('opening_hours', models.CharField(max_length=5)),
            ],
        ),
    ]
