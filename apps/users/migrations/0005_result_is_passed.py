# Generated by Django 4.2.5 on 2023-10-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_result_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='is_passed',
            field=models.BooleanField(default=False),
        ),
    ]