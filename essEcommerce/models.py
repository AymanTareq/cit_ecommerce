from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=512)
    mobile = models.CharField(max_length=12)

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

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank = True, null=True)
    status = models.BooleanField(default=False, blank=True,null=True)

    def __str__(self):
        return str(self.id)

    @property    
    def get_cart_total(self):
        total = self.orderitem_set.all()
        tot = 0
        for i in total:
            tot = tot + i.quantity
        return tot
    @property
    def get_cart_total_price(self):
        items = self.orderitem_set.all()
        tot = 0
        for i in items:
            tot = tot + i.total_price
        return tot


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True,null=True)

    def __str__(self):
        return self.product.name
        
    @property
    def total_price(self):
        total = self.product.price * self.quantity
        return total
    
    


