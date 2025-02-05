from django.shortcuts import render
from .models import Home,About
# Create your views here.
def home(request):
    homeall = Home.objects.all()
    about = About.objects.all()
    context={
        'home' : homeall,
        'about': about
    }
    return render(request,"index.html",context)

