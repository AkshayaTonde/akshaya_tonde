from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
import django.utils.timezone


def home(request):
    queryset = ContactsInfo.objects.all() 
    return render(request, "index.html", context={'page':'Contact Management', 'contactsInfo': queryset})


def createContact(request):
    context={'page':'Create Contact', "nameError": "","emailError":"" , "data":""}
    if request.method == "POST":
        data = request.POST
        if 'submit' in data:
            print(data)
            if ContactsInfo.objects.get(name=data.get("name")):
                context={"nameError": "Contact with this name already exists"}
                context={"Data": data}
                return render(request, "createContact.html", context) 
            
            if ContactsInfo.objects.get(name=data.get("email")):
                context={"emailError": "Contact with this email already exists"}
                return render(request, "createContact.html", context)
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
    // need to write logic for updating contact

    queryset = ContactsInfo.objects.get(id=id)
    context= {'contactsInfo': queryset, 'page' : 'Edit Contact'}
    return render(request, "editContact.html", context)