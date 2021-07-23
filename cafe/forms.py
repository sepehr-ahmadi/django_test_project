from django import forms

class CreateMenuItem(forms.Form):

    name=forms.CharField()
    price=forms.IntegerField()
    catagory=forms.CharField()
    discount=forms.IntegerField()
    serving_time_period=forms.TimeField()
    estimated_cooking_time=forms.TimeField()
    image=forms.ImageField()