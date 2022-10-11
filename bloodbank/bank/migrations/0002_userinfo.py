# Generated by Django 4.0.5 on 2022-10-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('mob', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=20)),
                ('bloodbgroup', models.CharField(max_length=20)),
                ('healthstatus', models.CharField(max_length=1000)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]