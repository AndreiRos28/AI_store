# Generated by Django 3.1.12 on 2025-04-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
