# Generated by Django 3.2.5 on 2022-11-23 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_issue',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 14, 16, 18, 114167), help_text='Date the book is due to'),
        ),
    ]
