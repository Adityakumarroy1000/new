from django.db import models


# Create your models here.
class Home(models.Model):
    Name = models.CharField( max_length=50)
    proffesion = models.CharField(max_length=300)

class About(models.Model):
    title = models.TextField()
    main_proffesion = models.CharField(max_length=100)
    shortdescription = models.TextField(max_length=200)
    website = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    Degree = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Freelance = models.CharField(max_length=50)
    birthdate = models.CharField( max_length=50)