# Generated by Django 4.0.2 on 2022-02-22 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterprojectapi', '0003_category_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='new',
        ),
    ]
