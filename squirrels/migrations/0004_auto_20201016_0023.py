# Generated by Django 3.1.2 on 2020-10-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0003_auto_20201016_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Date',
            field=models.DateField(help_text='Date of finding Squirrel (sighting)'),
        ),
    ]
