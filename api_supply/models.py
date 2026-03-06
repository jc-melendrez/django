from django.db import models
    
class Supplier(models.Model):
    name = models.TextField(max_length=100)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name