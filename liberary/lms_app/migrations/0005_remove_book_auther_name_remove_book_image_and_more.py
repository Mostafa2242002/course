# Generated by Django 5.0.1 on 2024-02-01 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0004_remove_category_rel_category_rel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='auther_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='number_of_pages',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rel',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lms_app.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rental_period',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rental_price_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]