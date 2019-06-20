from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me':"Hello, I am from views.py"} #httprequest response object
    return render(request, 'dash_app/index.html', context=my_dict)
