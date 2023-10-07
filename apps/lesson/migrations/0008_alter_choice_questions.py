# Generated by Django 4.2.5 on 2023-10-07 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0007_basemodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='lesson.question'),
        ),
    ]
