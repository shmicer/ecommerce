# Generated by Django 4.1.7 on 2023-03-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_manufacturer_item_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
