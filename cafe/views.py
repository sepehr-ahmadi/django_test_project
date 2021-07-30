from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views import View, generic
from django.forms import ModelForm

from .models import Orders, MenuItem, Table
# Create your views here.
from django.template import loader
from .forms import CreateMenuItem, LoginForm
from django.contrib.auth import views as auth_views



class LoginViews(View):
    def get(self, request, *args, **kwargs):
        print(request)
        return render(request, 'cafe/login.html')

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            print(user)
            return HttpResponse('ok')
        else:
            return HttpResponse('false')


class ProfileViews(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'auth.see_profile'

    def get(self, request, *args, **kwargs):
        pass


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         print(form)
#         user=authenticate(username=form.cleaned_data['user_name'],password=form.cleaned_data['password'])
#         print()
#         print(form.cleaned_data['user_name'])
#         print(form.cleaned_data['password'])
#         return HttpResponse('ok')
#     elif request.method == "GET":
#         form = LoginForm()
#         return render(request, 'cafe/login.html', {'form': form})
#
#     pass


def order_list(request):
    latest_orders_list = Orders.objects.all()
    print(Orders.objects.all())
    template = loader.get_template('cafe/order_list.html')
    context = {'latest_orders_list': latest_orders_list}
    return HttpResponse(template.render(context, request))


def order_detail(request, order_id):
    order_detail = Orders.objects.get(id=order_id)
    print(order_detail.menu_items.id)
    order_menu_item = MenuItem.objects.get(id=order_detail.menu_items.id)
    order_table = Table.objects.get(id=order_detail.table.id)

    context = {'order_detail': order_detail, 'order_menu_item': order_menu_item, 'order_table': order_table}
    template = loader.get_template('cafe/order_detail.html')

    return HttpResponse(template.render(context, request))


def ordering_menu(request):
    menu_item = MenuItem.objects.all()

    context = {'menu_item': menu_item}
    template = loader.get_template('cafe/ordered_menu.html')

    return HttpResponse(template.render(context, request))


# class OrderList(View):
#     def get(self, request, *args, **kwargs):
#         latest_orders_list = Orders.objects.all()
#         print(Orders.objects.all())
#         template = loader.get_template('cafe/order_list.html')
#         context = {'latest_orders_list': latest_orders_list}
#         return HttpResponse(template.render(context, request))
class OrderList(generic.ListView):
    template_name = 'cafe/order_list.html'
    context_object_name = 'latest_orders_list'

    def get_queryset(self):
        return Orders.objects.all()


# class OrderDetail(View):
#     def get(self, request, order_id, *args, **kwargs):
#         order_detail = Orders.objects.get(id=order_id)
#         print(order_detail.menu_items.id)
#         order_menu_item = MenuItem.objects.get(id=order_detail.menu_items.id)
#         order_table = Table.objects.get(id=order_detail.table.id)
#         context = {'order_detail': order_detail, 'order_menu_item': order_menu_item, 'order_table': order_table}
#         template = loader.get_template('cafe/order_detail.html')
#         return HttpResponse(template.render(context, request))

class OrderDetail(generic.DetailView):
    model = Orders
    template_name = 'cafe/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = kwargs['object']
        print(a.id)
        order_detail = Orders.objects.get(id=a.id)
        print(order_detail.menu_items.id)
        order_menu_item = MenuItem.objects.get(id=order_detail.menu_items.id)
        order_table = Table.objects.get(id=order_detail.table.id)
        context = {'order_detail': order_detail, 'order_menu_item': order_menu_item, 'order_table': order_table}
        return context


class OrderingMenu(View):
    def get(self, request, *args, **kwargs):
        menu_list = MenuItem.objects.all()
        print(menu_list)
        template = loader.get_template('cafe/ordered_menu.html')
        context = {'menu_list': menu_list}
        return HttpResponse(template.render(context, request))


def create_menu_item(request):
    if request.method == 'POST':
        form = CreateMenuItem(request.POST, request.FILES)
        print(form)
        # if form.is_valid():
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        catagory = form.cleaned_data['catagory']
        discount = form.cleaned_data['discount']
        serving_time_period = form.cleaned_data['serving_time_period']
        estimated_cooking_time = form.cleaned_data['estimated_cooking_time']
        image = form.cleaned_data['image']
        menu_item = MenuItem(name=name, price=price, catagory=catagory, discount=discount,
                             serving_time_period=serving_time_period, estimated_cooking_time=estimated_cooking_time,
                             image=image)
        menu_item.save()
        return HttpResponse('ok')
    elif request.method == "GET":
        form = CreateMenuItem()
        return render(request, 'cafe/create_menu_item.html', {'form': form})


class CreateMenuItemClassForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'catagory', 'discount', 'serving_time_period', 'estimated_cooking_time', 'image']


class CreateMenuItem_g(generic.FormView):
    form_class = CreateMenuItemClassForm
    template_name = 'cafe/create_menu_item.html'
    success_url = "https://google.com"

    def form_valid(self, form):
        f = form
        f.save()
        return super().form_valid(form)
