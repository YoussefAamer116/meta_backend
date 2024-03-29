# Generated by Django 4.2.7 on 2023-12-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_app', '0003_reservation_delete_logger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='count',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='booking_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
