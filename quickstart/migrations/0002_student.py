# Generated by Django 4.1.5 on 2023-01-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rol_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
