# Generated by Django 2.2.1 on 2019-05-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0003_auto_20190518_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='start_end',
            field=models.CharField(default='<django.db.models.fields.CharField>-<django.db.models.fields.CharField>', max_length=30),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_end',
            field=models.CharField(default='<django.db.models.fields.CharField>-<django.db.models.fields.CharField>', max_length=30),
        ),
    ]