# Generated by Django 3.0.5 on 2020-04-29 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
