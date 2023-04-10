from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)

    def __str__(self):
        return self.first_name+' '+self.last_name