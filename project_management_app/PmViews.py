from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from project_management_app.models import CustomUser, AdminPM, Staffs


def admin_home(request):
    context = {

    }
    return render(request, 'pm_template/home_content.html', context)


def admin_profile(request):
    pass


def manage_staff(request):
    staff = Staffs.objects.all()
    context = {
        "staff": staff
    }
    return render(request, 'pm_template/manage_staff_template.html', context)


def edit_staff(request):
    pass


def add_staff(request):
    return render(request, 'pm_template/add_staff_template.html')


def delete_staff(request, id):
    pass


def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, 'Invalid Method')
        return redirect("add_staff")
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  first_name=first_name, last_name=last_name, user_type='2')
            user.staff.address = address
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff')


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get('email')
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
