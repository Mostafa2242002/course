# Generated by Django 5.0.1 on 2024-02-01 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lms_app.book'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('romantic', 'Romantic'), ('horrible', 'Horrible'), ('adventure', 'Adventure')], max_length=50),
        ),
    ]