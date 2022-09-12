from logging import PlaceHolder
from django import forms

class ReviewForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=30)
    lname  = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email', max_length=50)
    review =forms.CharField(label='Please Drop Your Review Here:', max_length=120)