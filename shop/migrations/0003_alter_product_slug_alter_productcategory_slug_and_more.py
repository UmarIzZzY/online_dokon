# Generated by Django 5.0.3 on 2024-03-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, null=True),
        ),
    ]
