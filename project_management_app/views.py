from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect

from project_management_app.EmailBackEnd import EmailBackEnd
from . import models

# Create your views here.

def loginPage(request):
    return render(request,'login.html')


def doLogin(request):
    if request.method !="POST":
        return HttpResponse("<h2>Method not Allow</h2>")
    else:
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user !=None:
            login(request,user)
            user_type = user.user_type
            if user_type=="1":
                return redirect('admin_home')
            elif user_type=="2":
                return redirect("tl_home")
            elif user_type=="3":
                return redirect("tm_home")
            else:
                messages.error(request,"Invalid Login!")
                return redirect('login')
        else:
            messages.error(request,"Invalid Login Credentials!")
            return redirect("login")


def get_user_details(request):
        if request.user is not None:
            return HttpResponse("User : "+request.user.email+"User Type : "+request.user.user_type)
        else:
            return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")






