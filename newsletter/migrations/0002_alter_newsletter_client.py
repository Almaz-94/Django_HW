# Generated by Django 4.2.6 on 2023-10-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='client',
            field=models.ManyToManyField(related_name='newsletter', to='newsletter.client', verbose_name='Клиенты'),
        ),
    ]
