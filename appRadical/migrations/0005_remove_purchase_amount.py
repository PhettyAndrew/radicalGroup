# Generated by Django 3.0.5 on 2020-05-01 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appRadical', '0004_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='amount',
        ),
    ]
