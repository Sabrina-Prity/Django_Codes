# Generated by Django 5.1.3 on 2024-11-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Enter the musician's first name.", max_length=100)),
                ('last_name', models.CharField(help_text="Enter the musician's last name.", max_length=100)),
                ('email', models.EmailField(help_text='Enter email address.', max_length=254, unique=True)),
                ('phone', models.CharField(help_text='Enter phone number', max_length=12)),
                ('instrument_type', models.CharField(choices=[('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Drums', 'Drums'), ('Violin', 'Violin'), ('Flute', 'Flute'), ('Other', 'Other')], help_text='Select the type of instrument the musician plays.', max_length=20)),
            ],
        ),
    ]
