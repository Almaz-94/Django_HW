# Generated by Django 4.2.6 on 2023-10-13 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_category_created_at_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 10, 13, 14, 36, 1, 453940, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='last_change_date',
            field=models.DateField(auto_now=True),
        ),
    ]
