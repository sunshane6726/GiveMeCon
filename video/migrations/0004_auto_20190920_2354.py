# Generated by Django 2.2.1 on 2019-09-20 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='channel.Channel'),
        ),
    ]