from django.db import models

# Create your models here.

class Brands(models.Model):
    brand_name = models.CharField(max_length=100)
    county_origin = models.TextField()
    
    

    def __str__(self):
        return self.name