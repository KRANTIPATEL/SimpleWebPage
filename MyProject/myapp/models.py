from django.db import models

class FormData(models.Model):

    FullName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    PhoneNo = models.IntegerField()
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=500)






# Create your models here.
