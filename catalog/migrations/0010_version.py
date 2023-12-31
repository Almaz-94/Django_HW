# Generated by Django 4.2.6 on 2023-10-31 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(blank=True, default=1, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=250, verbose_name='Название версии')),
                ('is_current', models.BooleanField(choices=[(True, 'активная'), (False, 'не активная')], verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ('version_number',),
            },
        ),
    ]
