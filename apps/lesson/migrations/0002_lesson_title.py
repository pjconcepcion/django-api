# Generated by Django 4.2.5 on 2023-10-07 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]