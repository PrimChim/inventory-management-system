# Generated by Django 4.2 on 2023-05-01 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expirationdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='reorderpoint',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]