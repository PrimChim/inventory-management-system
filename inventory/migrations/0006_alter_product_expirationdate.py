# Generated by Django 4.2 on 2023-05-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_product_expirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expirationdate',
            field=models.DateField(),
        ),
    ]
