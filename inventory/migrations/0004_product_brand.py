# Generated by Django 4.2 on 2023-05-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_expirationdate_product_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
