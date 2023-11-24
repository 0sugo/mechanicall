from django.db import models

# Create your models here.
class Mechanic(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=40)
    carbrand = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname+" "+self.lastname

class ServiceRequest(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=40)
    faulty_part = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.location+" - "+self.faulty_part

class Tow(models.Model):
    id = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.companyname+" - "+self.location

class TowRequest(models.Model):
    id = models.AutoField(primary_key =True)
    location = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    def __str__(self):
        return self.location+" - "+self.destination