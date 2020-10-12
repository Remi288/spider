from django.db import models

# Create your models here.

class Login(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Name