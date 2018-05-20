from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from Registeration.forms import UserForm
from django.contrib.auth.models import User
from Registeration.models import Users
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def addUser(request):
    page_title = "Add User"
    form_class = UserForm
    if request.method == 'POST':
        form = form_class(request.POST,request.FILES)
        if form.is_valid():
            obj = User()
            obj.username = form.cleaned_data['username']
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.save()
            messages.success(request, 'User details saved successfully..!')
            return HttpResponse('Added')
    else:
        form = form_class()
    return render(request, 'users/usersform.html', {'form': form,'page_title':page_title})

def saveUser(request):
    # Save code for incoming data
    return HttpResponse("SaveUser")

def editUser(request,edit_id):
    # Get data and pass the value to view
    return HttpResponse(edit_id)

def updateUser(request):
    return HttpResponse("UpdateUser")

