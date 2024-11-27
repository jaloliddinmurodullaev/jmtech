# Generated by Django 5.1.3 on 2024-11-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('likes', models.BigIntegerField(default=0, null=True)),
                ('views', models.BigIntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('telegram', models.URLField()),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('firstname', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('about', models.TextField()),
                ('views', models.BigIntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=300)),
                ('link', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('views', models.BigIntegerField(default=0, null=True)),
            ],
        ),
    ]
