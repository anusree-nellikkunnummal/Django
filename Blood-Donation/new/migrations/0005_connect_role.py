# Generated by Django 3.2.5 on 2022-10-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_connect_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='role',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
