# Generated by Django 5.1.1 on 2024-10-11 20:25

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_desctiption_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]