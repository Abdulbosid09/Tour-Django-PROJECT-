from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="cat_image", null= True)

    def __str__(self):
        return self.name


class Airways(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    ava = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='avakomp')


class Davlatlar(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=250)
    about = models.CharField(max_length=255)
    image = models.ImageField(upload_to="dav_image", null=True)
    dav = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='davlatlar')

    def __str__(self):
        return self.name
    

