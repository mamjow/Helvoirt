# Generated by Django 2.2.6 on 2020-01-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('homepage', '0007_auto_20200115_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_header',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
