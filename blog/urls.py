from django.urls import path

from blog import views

urlpatterns = [
    path('profile/',views.profile ),
]
