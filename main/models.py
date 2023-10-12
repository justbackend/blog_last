from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text

# class
    
