from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
import django.utils.timezone


def home(request):
    queryset = ContactsInfo.objects.all() 

    return render(request, "index.html", context={'page':'Contact Management', 'contactsInfo': queryset})


def createContact(request):

    if request.method == "POST":
        data = request.POST
        print(data)
        ContactsInfo.objects.create(
            name = data.get("name"),
            email = data.get("emailadd"),
            notes = data.get("notes"),
            creation_date = django.utils.timezone.now()
        )
        return redirect('/viewContact')

    return render(request, "createContact.html", context)

def viewContact (request):

    queryset = ContactsInfo.objects.all()  
    print(queryset)
    context= {'contactsInfo': queryset, 'page': 'View Contact'}
    return render(request, "viewContact.html", context)

def deleteContact(request, id):
    queryset = ContactsInfo.objects.get(id=id)
    queryset.delete()
    return redirect('/')