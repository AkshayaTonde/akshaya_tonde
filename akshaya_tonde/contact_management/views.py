from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
import django.utils.timezone


def home(request):

    return render(request, "index.html", context={'page':'Contact Management'})


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
        return redirect('/')
        
    context = {'page': 'Create Contact'}
    return render(request, "createContact.html", context)

def viewContact (request):
    context = {'page': 'View Contact'}
    return render(request, "viewContact.html", context)