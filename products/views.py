from django.shortcuts import render

from django.http import HttpResponse

# Practicing git pull
def home(request):
    return render(request,"products/home.html")
