# Generated by Django 2.2.6 on 2019-11-17 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appearance'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='actor',
            field=models.CharField(default='', max_length=250),
        ),
    ]
