from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages
# first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     tuber_id = models.IntegerField()
#     tuber_name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     message = models.TextField(blank=True,max_length=255)
#     user_id = models.IntegerField(max_length=255)
# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            tuber_id = request.POST['youtuber_id']
            tuber_name = request.POST['tuber_name']
            city = request.POST['city']
            phone = request.POST['phone']
            state = request.POST['state']
            message = request.POST['message']
            user_id = request.POST['user_id']
            print(user_id)
            hiretubers = Hiretuber(first_name=first_name,last_name=last_name,email=email,tuber_id=tuber_id,tuber_name=tuber_name,city=city,phone=phone,state=state,message=message,user_id=user_id)
            hiretubers.save()
            messages.success(request,"Thank you for reaching out!")
            return redirect('youtubers')
