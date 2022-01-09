from django.core.checks import messages
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views



# Create your views here.
def joinin(request):
    #Getting post parameter from joinin.html
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

    #Performing checking
        if User.objects.filter(username = username).exists():
            messages.error(request,'* Username is already taken')
            return redirect('joinin')

        elif User.objects.filter(email = email).exists():
            messages.warning(request,'* Email is already Register')
            return redirect('joinin')
    #creating user
        else:
            myuser = User.objects.create_user(username=username,email=email,password=password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            # messages.success(request, 'Your account has been created successfully')
            return render(request,'accountsuccess.html')
        
    else:
        return render(request,'joinin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password= password)

        if user is not None:
            auth_login(request,user)

            return redirect('/authuser/home')
            
            
        else:
            messages.warning(request,"Bad Credentials!")
            return render(request,'login.html')

    return render(request,'login.html')


