# Generated by Django 4.2.7 on 2023-12-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slogan',
            field=models.CharField(max_length=80),
        ),
    ]
