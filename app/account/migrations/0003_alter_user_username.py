# Generated by Django 4.1.7 on 2023-03-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=50),
        ),
    ]