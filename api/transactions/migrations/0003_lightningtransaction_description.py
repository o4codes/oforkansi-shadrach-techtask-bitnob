# Generated by Django 4.0.3 on 2022-03-25 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_remove_lightningtransaction_lightening_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightningtransaction',
            name='description',
            field=models.CharField(default='Payments', max_length=100),
        ),
    ]
