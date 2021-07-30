from django import forms
from django.core.exceptions import ValidationError


def name_validator(name:str):
    for char in name:
        if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
            raise ValidationError('enter correct name')
class CreateMenuItem(forms.Form):

    name=forms.CharField(max_length=40,help_text='enter name of food',required=True,validators=[])
    price=forms.IntegerField(validators=[],required=True,help_text='enter the price')
    catagory=forms.CharField()
    discount=forms.IntegerField()
    serving_time_period=forms.TimeField()
    estimated_cooking_time=forms.TimeField()
    image=forms.ImageField()

class LoginForm(forms.Form):
    user_name=forms.CharField(max_length=40,help_text="enter username")
    password=forms.CharField(max_length=40,help_text="enter password")