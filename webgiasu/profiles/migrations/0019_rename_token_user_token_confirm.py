# Generated by Django 3.2.5 on 2021-09-10 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_alter_user_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='token',
            new_name='token_confirm',
        ),
    ]
