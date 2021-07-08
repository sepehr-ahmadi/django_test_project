from django.db import models


# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=30)


class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    catagory = models.CharField(max_length=30)
    discount = models.IntegerField()
    serving_time_period = models.TimeField()
    estimated_cooking_time = models.TimeField()


class Orders(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    number = models.IntegerField()
    status = models.fields.CharField(max_length=30)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birthday = models.DateField()


class Receipts(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ueser=models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    final_price = models.IntegerField()
    time_stamp = models.TimeField()
