from django.db import models

# Create your models here.
class Student(models.Model):
    # store the image
    image = models.ImageField(upload_to='images/')
    # images, 
    # summary
    summary  = models.CharField(max_length=200)