# Generated by Django 5.1.6 on 2025-02-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='default_user', max_length=150, unique=True),
        ),
    ]
