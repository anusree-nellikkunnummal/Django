# Generated by Django 4.0.5 on 2022-10-12 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0003_connect_lastdate_connect_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
    ]