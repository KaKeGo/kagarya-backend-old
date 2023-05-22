# Generated by Django 4.2.1 on 2023-05-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_showapiurl_api_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='showapiurl',
            name='access',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Authenticated user', 'Authenticated user'), ('Any', 'Any')], default='Admin', max_length=20),
        ),
    ]