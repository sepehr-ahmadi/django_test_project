from django.test import TestCase
from .models import MenuItem,TimestampMixin
# Create your tests here.
class MenuItemTest(TestCase):
    def test_menu_item_final_price_negative_discount(self):
        pass
    def test_menu_item_final_price_discount_greater_than_price(self):
        pass
    def test_menu_item_final_price_empty_discount(self):
        pass
    def test_menu_item_final_price_negative_price(self):
        pass
class TimeStampMixinTest(TestCase):
    def test_none(self):
        pass
    def test_now(self):
        pass
    def test_future(self):
        pass
