from django.core.exceptions import ValidationError


def menu_item_price_validator(value):
    if value < 0:
        raise ValidationError('menu item price invalid')

    pass
