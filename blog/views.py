from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader


def profile(request):
    template = loader.get_template('blog/my_profile.html')

    return HttpResponse(template.render())
