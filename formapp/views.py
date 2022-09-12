from copyreg import constructor
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import ReviewForm

# Create your views here.

def fome(request):
    return HttpResponse("Form under construction!")

def rental_review(request):
    if (request.method == 'POST'):
        form = ReviewForm(request.POST)
        
        if  form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('formapp:thanks'))
            
    else:
        form = ReviewForm()
        return render(request,'formapp/rental_review.html', context={'form':form})
        

def thanks(request):
    return render(request,'formapp/thankyou.html')