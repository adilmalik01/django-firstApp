# Generated by Django 5.1.1 on 2024-10-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
    ]
