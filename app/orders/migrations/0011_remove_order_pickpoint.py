# Generated by Django 4.1.7 on 2023-03-20 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_pickpoint_alter_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pickpoint',
        ),
    ]
