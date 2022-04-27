# Generated by Django 3.2.5 on 2021-09-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_rename_token_user_token_confirm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token_confirm',
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
