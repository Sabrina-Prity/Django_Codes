from django.db import models

class Musician(models.Model):
   
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Drums', 'Drums'),
        ('Violin', 'Violin'),
        ('Flute', 'Flute'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254, unique=True)
    phone = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=20,choices=INSTRUMENT_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
