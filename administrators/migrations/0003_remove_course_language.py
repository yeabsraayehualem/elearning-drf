# Generated by Django 4.2.4 on 2024-04-25 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0002_rename_tyle_booktype_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='language',
        ),
    ]