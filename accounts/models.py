from django.db import models

# Create your models here.
class userList(models.Model):
    id = models.CharField(max_length= 25,unique = False ,primary_key=True)
    password = models.CharField(max_length= 25,unique = True ,) 
