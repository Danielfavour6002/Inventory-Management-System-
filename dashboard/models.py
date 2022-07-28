
from sre_constants import CATEGORY 
from django.contrib.auth.models import User

from django.db import models
# from sre_constants import 


# Create your models here.

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),

)

LABEL_STATUS = (
    ('Received', 'Received'),
    ('In-progress', 'In-progress'),
    ('Delivered', 'Delivered'),
    ('Declined', 'Declined'),
)
class Product(models.Model):
    name = models.CharField(max_length=225, null=True)
    category = models.CharField(max_length=225, choices= CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'


    def __str__(self):
        return f'{self.name}--{self.quantity}'
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    # date = models.TimeField(auto_now_add=True)
    
    status = models.CharField(max_length=225, choices= LABEL_STATUS, null=True, default= 'In-progress')

    
    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff}'