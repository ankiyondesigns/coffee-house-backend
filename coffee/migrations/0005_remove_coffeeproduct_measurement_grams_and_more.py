# Generated by Django 5.1.5 on 2025-01-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_alter_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeeproduct',
            name='measurement_grams',
        ),
        migrations.AddField(
            model_name='coffeeproduct',
            name='measurement_unit',
            field=models.CharField(blank=True, choices=[('kg', 'Kilograms'), ('mg', 'Milligrams'), ('g', 'Grams')], max_length=2, null=True),
        ),
    ]
