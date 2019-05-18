# Generated by Django 2.2.1 on 2019-05-18 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientride',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clientride',
            name='ride',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='ride',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='ride',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='ClientRide',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]