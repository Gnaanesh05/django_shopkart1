# Generated by Django 4.2.1 on 2023-06-28 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Catagory',
            new_name='category',
        ),
    ]
