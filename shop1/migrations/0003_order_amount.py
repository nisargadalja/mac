# Generated by Django 3.0.4 on 2020-04-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_desc1'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
