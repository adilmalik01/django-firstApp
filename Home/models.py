from django.db import models

# Create your models here.
class Book(models.Model):
    authoName =  models.CharField(max_length=20)
    title =  models.TextField()
    description =  models.TextField()
    
    
    def __str__(self):
        return self.title + " " + self.authoName
    
    
    
class product(models.Model):
    productName =  models.CharField(max_length=20)
    productPrice =  models.TextField()
    
    
    def __str__(self):
        return self.productName