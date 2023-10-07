from django.db import models

# Create your models here.
class Business(models.Model):  
    bid = models.CharField(max_length=20,unique=True)  
    bname = models.CharField(max_length=100)  
    bemail = models.EmailField()  
    bownerinfo = models.CharField(max_length=100)
    baddressl1 = models.CharField(max_length=100)  
    baddressl2 = models.CharField(max_length=100) 
    bsize = models.IntegerField()
    class Meta:  
        db_table = "business"  