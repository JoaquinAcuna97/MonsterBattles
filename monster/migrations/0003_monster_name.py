# Generated by Django 3.2.16 on 2024-04-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monster", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='name',
            field=models.CharField(default='A monster', max_length=100),
        ),
    ]
