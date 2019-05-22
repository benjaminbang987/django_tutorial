from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<!DOCTYPE html> "
                        "<html> "
                        "   <head> "
                        "       <title>My Website</title>"
                        "   </head>"
                        "<body>"
                        "   <h1> Hello, World. Wecome to the polls index.<h2> "
                        "   </br>"
                        "</body>")
