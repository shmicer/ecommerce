# Generated by Django 4.1.7 on 2023-03-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=1, max_length=254, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
    ]
