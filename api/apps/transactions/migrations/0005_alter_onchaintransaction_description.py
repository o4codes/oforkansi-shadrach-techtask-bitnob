# Generated by Django 4.0.3 on 2022-03-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_delete_onchainaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onchaintransaction',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
