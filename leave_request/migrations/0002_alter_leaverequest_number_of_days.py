# Generated by Django 3.2 on 2022-02-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='number_of_days',
            field=models.PositiveIntegerField(),
        ),
    ]
