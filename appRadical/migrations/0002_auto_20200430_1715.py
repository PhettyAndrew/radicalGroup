# Generated by Django 3.0.5 on 2020-04-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRadical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='electrical_drawingImage',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='plan',
            name='plumbing_drawingImage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
