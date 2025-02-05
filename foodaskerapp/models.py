from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name= "restaurant")
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length= 15)
    logo = models.ImageField(upload_to='restaurant_logos/', null=True, blank=True)
   
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="MenuItem")
    Name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Name

class OrderDetails(models.Model):
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="OrderDetails")
    customername = models.CharField(max_length=100)
    customeremail = models.EmailField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.MenuItem.Name

class Delivery(models.Model):
    OrderDetails = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name="Delivery")
    address = models.CharField(max_length=255)
    delivery_status = models.CharField(
     max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Delivered', 'Delivered')], default='Pending'
    )
    delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.OrderDetails.customername

    