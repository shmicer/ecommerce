# Generated by Django 4.1.7 on 2023-03-10 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_item_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]
