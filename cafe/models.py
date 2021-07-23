import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from cafe import validator


class Table(models.Model):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=30)


class MenuItem(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, help_text='enter your menu item name:')
    price = models.IntegerField(null=False, help_text='please enter price of item', verbose_name='price(irr)',
                                validators=[validator.menu_item_price_validator])
    catagory = models.CharField(max_length=30)
    image = models.ImageField(upload_to='menu_item/img')
    discount = models.IntegerField()
    creat_time_stamp = models.DateTimeField(auto_now_add=True, editable=True)
    modified_time_stamp = models.DateTimeField(auto_now=True, editable=True)
    serving_time_period = models.TimeField()
    estimated_cooking_time = models.TimeField()

    def final_price(self, price, discount):
        return price * (1 - discount / 100)

    def __str__(self):
        return f'{self.id}# {self.name} {self.price}'


class Orders(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    number = models.IntegerField()
    status = models.fields.CharField(max_length=30)

    @classmethod
    def filter_by_menuitem(cls, menu_item):
        res = cls.objects.filter(menu_items__name=menu_item)
        return res


class TimestampMixin(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        abstract = True


class Timestamp(TimestampMixin):
    def logical_delete(self):
        self.delete_timestamp = datetime.datetime.now()


class Cashier(User, TimestampMixin):
    phone_number = models.CharField(max_length=11)
    national_code = models.CharField(max_length=11)
    Address = models.TextField()


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birthday = models.DateField()


class Receipts(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ueser = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    final_price = models.IntegerField()
    time_stamp = models.TimeField()
