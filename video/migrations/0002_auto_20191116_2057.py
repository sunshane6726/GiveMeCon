# Generated by Django 2.2.5 on 2019-11-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='content',
        ),
        migrations.AddField(
            model_name='video',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video_num',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
