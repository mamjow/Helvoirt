# Generated by Django 2.2.6 on 2020-01-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('homepage', '0005_auto_20200103_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_header',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
