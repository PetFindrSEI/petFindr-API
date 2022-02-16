from django.db import models
from phone_field import PhoneField

# Create your models here.
class Pet(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]
    TYPE_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Uk', 'Unknown'),
    ]
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    MICROCHIP_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
        ('Uk', 'Unknown'),
    ]

    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    name = models.CharField(max_length=100, default='Unknown')
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Dog')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES)
    color = models.CharField(max_length=100)
    description = models.TextField()
    microchip = models.CharField(max_length=100, choices=MICROCHIP_CHOICES, default='Unknown')
    location = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    reported_time = models.DateTimeField()

    owner = models.ForeignKey('users.User', related_name='pets', on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='images/', default='images/default.png')

    phone_number = PhoneField(blank=True, help_text='Contact Phone Number')

    def __str__(self):
        return f'{self.name} - {self.status} - {self.type}'