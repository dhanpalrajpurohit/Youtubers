from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are in loggedin.")
            return redirect("dashboard")
        else:
            messages.warning(request,"Username and Password is not correct.")
            return redirect("login")

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"Username is already exits.")
                #print("*********************Username********************")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,"email is already exits.")
                    #print("*******************email**********************")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user.save()
                    #print("*****************************************")
                    messages.success(request,'Registered Successfully.')
                    return redirect('home')

        else:
            messages.warning(request,"password does not match")
            return redirect('register')
        
    return render(request, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('home')
    