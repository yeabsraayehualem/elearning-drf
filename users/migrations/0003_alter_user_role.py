# Generated by Django 4.2.4 on 2024-04-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Student', 'Student'), ('Teacher', 'Teacher')], default='Student', max_length=50),
        ),
    ]
