# Generated by Django 4.1.7 on 2023-04-20 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_name',
            new_name='User_name',
        ),
    ]
