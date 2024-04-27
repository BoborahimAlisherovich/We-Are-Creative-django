

from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    return render(request, "index.html" )

def components_view(request):
    return render(request, "components.html" )


