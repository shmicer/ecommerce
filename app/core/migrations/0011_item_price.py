# Generated by Django 4.1.7 on 2023-03-10 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=10000),
            preserve_default=False,
        ),
    ]
