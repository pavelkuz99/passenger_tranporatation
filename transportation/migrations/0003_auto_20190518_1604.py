# Generated by Django 2.2.1 on 2019-05-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0002_auto_20190518_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='start_end',
            field=models.CharField(default='<django.db.models.fields.CharField>-><django.db.models.fields.CharField>', max_length=30),
        ),
        migrations.AddField(
            model_name='route',
            name='start_end',
            field=models.CharField(default='<django.db.models.fields.CharField>-><django.db.models.fields.CharField>', max_length=30),
        ),
    ]
