from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    contact_list =[
        {'Contact_name':'Akshaya', 'email':'akshaya@gmail.com','CreatedTime':'021545'},
        {'Contact_name':'Mahan', 'email':'mohan@test.com','CreatedTime':'021545'},
        {'Contact_name':'Swapnil', 'email':'swaps@test.com','CreatedTime':'021545'}

    ]

    return render(request, "index.html", context={'contact_list': contact_list})


