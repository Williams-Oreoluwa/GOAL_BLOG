# Generated by Django 4.1.3 on 2022-12-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
