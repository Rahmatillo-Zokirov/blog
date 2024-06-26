# Generated by Django 5.0.4 on 2024-04-20 05:57

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
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('photo', models.FileField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Talks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('photo', models.FileField(upload_to='photos')),
                ('url', models.URLField()),
            ],
        ),
    ]
