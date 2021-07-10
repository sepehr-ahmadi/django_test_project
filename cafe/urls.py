from django.urls import path

from cafe import views

urlpatterns = [
    path('order_list/',views.order_list ,name='order_list'),
    path('<int:order_id>/',views.order_detail,name='order_detail' ),
    path('ordering_menu/',views.ordering_menu,name='orderign_menu')
]
