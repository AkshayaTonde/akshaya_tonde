from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
import django.utils.timezone
from django.contrib import messages


def home(request):
    queryset = ContactsInfo.objects.all() 
    return render(request, "index.html", context={'page':'Contact Management', 'contactsInfo': queryset})


def createContact(request):
    context={'page':'Create Contact'}

    if request.method == "POST":
        data = request.POST
        form_name = data.get("name")
        form_email = data.get("emailadd")

        if 'submit' in data:
            
            if ContactsInfo.objects.filter(name__iexact=form_name).exists():
                messages.error(request, f"Contact with {form_name} already exists")
                return render(request,"createContact.html" )
            
            if ContactsInfo.objects.filter(name__iexact=form_email).exists():
                messages.error(request, f"Contact with {form_email} already exists")
                return render(request,"createContact.html" )
            else:

                ContactsInfo.objects.create(
                        name = data.get("name"),
                        email = data.get("emailadd"),
                        notes = data.get("notes"),
                        creation_date = django.utils.timezone.now()
                )
                return redirect('/')
          
        if 'cancel' in data:
            return redirect('/')
        
    return render(request, "createContact.html", context)

def viewContact (request, id):
    queryset = ContactsInfo.objects.get(id=id)
    print(queryset)
    context= {'contactsInfo': queryset, 'page': 'View Contact'}

    if request.method == "POST":
        data = request.POST
        if 'home' in request.POST:
            return redirect('/')
        
        if 'edit' in request.POST:
            id = data.get("id")
            return redirect(f'editContact/{id}')
        
        if 'delete' in request.POST:
            return redirect(f'deleteContact/{id}')

    return render(request, "viewContact.html", context)

def deleteContact(request, id):

    queryset = ContactsInfo.objects.get(id=id)
    print(queryset)
    context= {'contactsInfo': queryset, 'page': 'Delete Contact'}

    if request.method == "POST":
        if 'delete' in request.POST:
            queryset = ContactsInfo.objects.get(id=id)
            queryset.delete()
            return redirect('/')
        if 'cancel' in request.POST:
            return redirect('/')
        
    return render(request, "deleteContact.html", context)

def editContact(request, id):
    queryset = ContactsInfo.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        if 'edit' in request.POST:
            queryset = ContactsInfo.objects.get(id=id)
            queryset.name= data.get("name")
            queryset.email =  data.get("emailadd")
            queryset.notes = data.get("notes")
            queryset.creation_date = django.utils.timezone.now()
            queryset.save()
            return redirect('/')
        if 'cancel' in request.POST:
            return redirect('/')
        
    context= {'contactsInfo': queryset, 'page' : 'Edit Contact'}
    return render(request, "editContact.html", context)