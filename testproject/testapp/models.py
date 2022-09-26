from django.db import models

# Create your models here.
class Mkoa(models.Model):
    name = models. CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Wilaya(models.Model):
    jinalamkoa= models.ForeignKey('Mkoa', on_delete=models.CASCADE) 
    jinalawilaya= models.CharField(max_length=50)
    
    def __str__(self):
        return self.jinalawilaya
      
      
class Mazao(models.Model):
    jinalawilaya= models.ManyToManyField(Wilaya) 
    jinalamazao= models.CharField(max_length=50)
    
    def __str__(self):
        return self.jinalamazao      