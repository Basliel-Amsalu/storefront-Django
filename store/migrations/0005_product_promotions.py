# Generated by Django 5.0.4 on 2024-04-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_last_updated_product_last_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(to='store.promotion'),
        ),
    ]