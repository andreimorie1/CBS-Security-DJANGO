from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('unset','Unset'),
    ('stationary','Stationary'),
    ('electronics','Electronics'),
    ('food','Food')
)
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, choices=CATEGORY, default='unset')
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE)
    order_quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return f'{self.product} Handled by {self.staff.username}'