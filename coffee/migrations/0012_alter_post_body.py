# Generated by Django 5.1.5 on 2025-02-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0011_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
