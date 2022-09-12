from django.urls import path
from . import views

app_name = 'formapp'

urlpatterns = [
     path('',views.fome,name='fome'),
    path('thanks',views.thanks,name='thanks'),
    path('rental_review',views.rental_review,name='rental_review'),
    ]
