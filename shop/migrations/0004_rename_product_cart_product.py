# Generated by Django 4.2.1 on 2023-06-30 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_catagory_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Product',
            new_name='product',
        ),
    ]
