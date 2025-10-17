from django.shortcuts import render, HttpResponse
# inbuilt form   
from django.contrib.auth.forms import UserCreationForm


def home(req):
    return HttpResponse("Hello Home")

def register(req):
    form=UserCreationForm
    if req.method=="POST":
        regform=UserCreationForm(req.POST)
        if regform.is_valid():
            regform.save()
            # we can see data stored in admin panel under home->user. 
    return render(req,'register.html',{'form':form})