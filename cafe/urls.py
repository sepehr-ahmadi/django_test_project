from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LoginView

from cafe import views


urlpatterns = [
    path('order_list/', views.order_list, name='order_list'),
    path('<int:pk>/', views.OrderDetail.as_view(), name='OrderDetail'),
    path('ordering_menu/', views.ordering_menu, name='ordering_menu'),
    path('OrderingMenu/', views.OrderingMenu.as_view(), name='OrderingMenu'),
    path('OrderList/', views.OrderList.as_view(), name='OrderList'),
    path('OrderDetail/', views.OrderingMenu.as_view(), name='OrderingMenu'),
    path('create_menu_item',views.create_menu_item,name='create_menu_item'),
    path('createmenuitem',views.CreateMenuItem_g.as_view(),name='create_menu_item'),
    # path('login',views.LoginViews.as_view(),name='login'),
    path('profile',views.ProfileViews.as_view(),name='profile'),
    path('django_login/',include('django.contrib.auth.urls')),
    # path('django_login/login/',LoginView.as_view()),

]