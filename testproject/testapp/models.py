from django.db import models

# Create your models here.
# ***************************CATEGORIES********************************

class Category(models.Model):
    kundi = models.CharField(max_length=50)
    
    def __str__(self):
        return self.kundi
    
class Subcategory(models.Model):
    kundi = models.ForeignKey('Category', on_delete=models.CASCADE)
    kundijina = models.CharField(max_length=50)  
    image = models.ImageField(upload_to="uploads/",null=True, blank=True)
    
    def __str__(self):
        return self.kundijina
    
class  Subcategoryinfo(models.Model):
    kundijina = models.ForeignKey('Subcategory', on_delete=models.CASCADE)    
    taarifazakundi = models.TextField()
    
    def __str__(self):
        return self.taarifazakundi

# **********************************************************************
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
# *******************************************************************************************
class Udongo(models.Model):
    jinalawilaya= models.ManyToManyField(Wilaya) 
    jinalaudongo= models.CharField(max_length=50)
    
    def __str__(self):
        return self.jinalaudongo       
    
class Udongotaarifa(models.Model):
    ainayaudongo = models.ForeignKey('Udongomakundi', on_delete=models.CASCADE)   
    taarifazake = models.TextField()
    
    def __str__(self):
        return self.taarifazake
    
class Udongomakundi(models.Model):
    ainayaudongo = models. CharField(max_length=50)
    
    def __str__(self):
        return self.ainayaudongo    