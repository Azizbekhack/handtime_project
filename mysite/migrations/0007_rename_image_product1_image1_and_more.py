# Generated by Django 5.0.6 on 2024-08-15 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_product1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product1',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='product1',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='product1',
            old_name='price',
            new_name='price1',
        ),
    ]
