# Generated by Django 3.2.12 on 2023-07-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_ready_to_distribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ready_to_distribute',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=10),
        ),
    ]
