# Generated by Django 5.0.3 on 2024-03-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
