# Generated by Django 3.1.7 on 2021-03-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0004_auto_20210313_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='CreatedDate',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='ModifiedDate',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
    ]
