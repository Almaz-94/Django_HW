# Generated by Django 4.2.6 on 2023-10-20 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
