from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
import datetime


def home(request):

    return render(request, "index.html", context={'page':'Contact Management'})


def createContact(request):

    data = request.POST 

    print(data)

    ContactsInfo.objects.create(
        name = data.get("name"),
        email = data.get("emailadd"),
        notes = data.get("notes"),
        creation_date = datetime.datetime.now()
    )
    context = {'page': 'Create Contact'}
    return render(request, "createContact.html", context)

def viewContact (request):
    context = {'page': 'View Contact'}
    return render(request, "viewContact.html", context)