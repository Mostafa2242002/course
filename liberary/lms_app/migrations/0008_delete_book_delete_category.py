# Generated by Django 5.0.1 on 2024-02-03 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0007_category_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
