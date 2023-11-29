from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
import datetime


def home(request):

    contact_list =[
        {'Contact_name':'Akshaya', 'email':'akshaya@gmail.com','CreatedTime':'021545'},
        {'Contact_name':'Mahan', 'email':'mohan@test.com','CreatedTime':'021545'},
        {'Contact_name':'Swapnil', 'email':'swaps@test.com','CreatedTime':'021545'}

    ]

    return render(request, "index.html", context={'page':'Contact Management','contact_list': contact_list})


def createContact(request):

    data = request.POST 

    contact_Details.objects.create(
        name = data.get("name"),
        email = data.get("email"),
        notes = data.get("notes"),
        creation_date = datetime.datetime.now()
    )
   

    context = {'page': 'Create Contact'}
    return render(request, "createContact.html", context)

def viewContact (request):
    context = {'page': 'View Contact'}
    return render(request, "viewContact.html", context)