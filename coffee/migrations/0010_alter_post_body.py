# Generated by Django 5.1.5 on 2025-02-15 11:32

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
