# Generated by Django 5.1.3 on 2024-12-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car/media/uploads/'),
        ),
    ]
