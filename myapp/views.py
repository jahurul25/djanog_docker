from django.shortcuts import render

# Create your views here.

def home(request):
    print("Django docker run successfully")
    return render(request, "home.html")