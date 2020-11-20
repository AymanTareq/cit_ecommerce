from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=250, null=True,blank=True)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})

