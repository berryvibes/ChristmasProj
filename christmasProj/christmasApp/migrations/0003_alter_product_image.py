# Generated by Django 5.1.3 on 2025-02-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmasApp', '0002_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='imag/'),
        ),
    ]
