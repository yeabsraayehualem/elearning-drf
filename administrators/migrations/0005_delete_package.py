# Generated by Django 4.2.4 on 2024-05-05 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_delete_subscription'),
        ('administrators', '0004_course_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Package',
        ),
    ]
