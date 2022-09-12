from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render

def dchome(request):
    try:
        return HttpResponseRedirect(reverse('formapp:rental_review'))
    except:
        return HttpResponse('Not available!')