# Generated by Django 4.2.6 on 2023-10-13 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id', 'name'), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id', 'name'), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]