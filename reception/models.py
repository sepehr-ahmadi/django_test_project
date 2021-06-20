class menu_item(object):
    def __init__(self, id, name, price, catagory, discount, serving_time_period, estimated_cooking_time):
        self.id = id
        self.name = name
        self.price = price
        self.catagory = catagory
        self.discount = discount
        self.serving_time_period = serving_time_period
        self.estimated_cooking_time = estimated_cooking_time


class orders():
    def __init__(self, id, table, menu_items, number, status):
        self.id = id
        self.table = table
        self.menu_items = menu_items
        self.number = number
        self.status = status


class reciept():
    def __init__(self, id, order, total_price, final_price, time_stamp):
        self.id = id
        self.order = order
        self.total_price = total_price
        self.final_price = final_price
        self.time_stamp = time_stamp
