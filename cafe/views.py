from django.http import HttpResponse
from django.shortcuts import render
from .models import Orders,MenuItem,Table
# Create your views here.
from django.template import loader


def order_list(request):
    latest_orders_list = Orders.objects.all()
    print(Orders.objects.all())
    template = loader.get_template('cafe/order_list.html')
    context = {'latest_orders_list': latest_orders_list}
    return HttpResponse(template.render(context, request))


def order_detail(request, order_id):
    order_detail = Orders.objects.get(id=order_id)
    print(order_detail.menu_items.id)
    order_menu_item=MenuItem.objects.get(id=order_detail.menu_items.id)
    order_table=Table.objects.get(id=order_detail.table.id)

    context = {'order_detail':order_detail,'order_menu_item':order_menu_item,'order_table':order_table}
    template = loader.get_template('cafe/order_detail.html')

    return HttpResponse(template.render(context, request))

def ordering_menu(request):
    menu_item = MenuItem.objects.all()

    context = {'menu_item':menu_item}
    template = loader.get_template('cafe/ordered_menu.html')

    return HttpResponse(template.render(context, request))

