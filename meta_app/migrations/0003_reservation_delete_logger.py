# Generated by Django 4.2.7 on 2023-11-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_app', '0002_logger_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=200, verbose_name='Phone number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Logger',
        ),
    ]
