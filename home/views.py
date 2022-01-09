from django.shortcuts import redirect, render
from home.models import Contact
from  datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):

    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent.')


    return render(request,'contact.html')
    

def about(request):
     return render(request,'about.html')   

def cmail(request):
    return render(request,'cmail.html')

