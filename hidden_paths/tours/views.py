from django.shortcuts import render
from .models import Tours
from django.db import models

# Create your views here.
def principal(request):
    tours=Tours.objects.all()
    return render(request, "tours/principal.html",{'tours':tours})




