from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=False)
    photo = models.ImageField(upload_to= 'photos/', default=None, blank=True)

    def __str__(self):
        return (self.name)

