# Generated by Django 2.2.1 on 2019-05-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_auto_20190518_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='route',
            options={'ordering': ('start_end',)},
        ),
        migrations.RemoveField(
            model_name='ride',
            name='end',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='start',
        ),
        migrations.RemoveField(
            model_name='route',
            name='end',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start',
        ),
        migrations.AlterField(
            model_name='ride',
            name='start_end',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_end',
            field=models.CharField(default='', max_length=30),
        ),
    ]
