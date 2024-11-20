from django.db import models

# Create your models here.
class Student(models.Model):
    # id= models.AutoField()
    name=models.CharField(max_length=100)
    age= models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    # image=models.ImageField()
    file= models.FileField()


class Product(models.Model):
    product_name = models.TextField()
    product_title = models.CharField(max_length=200, default="Untitled") 
    product_price = models.IntegerField(default=0) 

class Car(models.Model):
    car_name =models.CharField(max_length=100)
    car_speed =models.IntegerField()

    def __str__(self):
        return self.car_name