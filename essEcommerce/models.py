from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(512)
    mobile = models.CharField(12)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=250, null=True,blank=True)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    @property
    def img(self):
        try:
            img_url = self.image.url
        except:
            img_url = ''
        return img_url

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

