from django.db import models
from django.core.validators import *
from django.core import validators
# from django.contrib.auth.models import User

class Catagoery(models.Model):
    catagoery_name = models.CharField(max_length=200, null= True,validators=[validators.MinLengthValidator(2)])
    catagoery_description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.catagoery_name

class Food(models.Model):
    food_name = models.CharField(max_length=200)
    food_price = models.FloatField()
    food_image = models.FileField(upload_to='static/uploads')
    catagoery = models.ForeignKey(Catagoery, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.food_name

# class Cart(models.Model):
#     meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#
# class Order(models.Model):
#     STATUS = (
#         ('Pending', 'Pending'),
#         ('Delivered', 'Delivered'),
#     )
#     PAYMENT = (
#         ('Cash On Delivery', 'Cash On Delivery'),
#         ('Esewa', 'Esewa'),
#         ('Khalti', 'Khalti'),
#     )
#     meals = models.ForeignKey(Meals, null=True, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
#     total_price = models.IntegerField(null=True)
#     status = models.CharField(max_length=200, choices=STATUS, null=True)
#     payment_method = models.CharField(max_length=200, choices=PAYMENT, null=True)
#     payment_status = models.BooleanField(default=False, null=True, blank=True)
#     contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
#     contact_address = models.CharField(max_length=200, null=True)
#     created_date = models.DateTimeField(auto_now_add=True, null=True)

















