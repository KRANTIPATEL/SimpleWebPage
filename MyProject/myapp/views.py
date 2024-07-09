from django.shortcuts import render
from datetime import datetime
import random
from .models import FormData
from django.http import HttpResponse

def home(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    quote = get_random_quotes()

    context = {
        'current_time': current_time,
        'quotes':quote
    }
    return render(request, 'home.html', context)

def form(request):
        
        if request.method == 'POST':

            name = request.POST['fullname']
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            msg = request.POST['message']

            details = FormData(FullName=name , Email=email , PhoneNo=phone 
                           , Subject=subject , Message=msg )
            details.save()
            return HttpResponse("Submit successfully! <a href='/display/'>Go to Display Data</a>")


        return render(request,'form.html')

def get_random_quotes():
    quotes = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    ]
    return random.choice(quotes)

def display(request):
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        filtered_data = FormData.objects.filter(FullName__icontains=search_term)
    else:
        filtered_data = FormData.objects.all()
    
    context = {
        'filtered_data': filtered_data
    }
    return render(request, 'display.html', context)

# Create your views here.
