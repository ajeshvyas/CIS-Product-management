# Generated by Django 2.2.4 on 2021-04-07 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20210407_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table=None,
        ),
    ]