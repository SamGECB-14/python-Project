# Generated by Django 4.1.5 on 2023-01-13 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_singer_song'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='singer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='singer',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='singer',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='SingerImages/'),
        ),
        migrations.RemoveField(
            model_name='song',
            name='singer',
        ),
        migrations.AddField(
            model_name='song',
            name='singer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='song', to='quickstart.singer'),
        ),
    ]
