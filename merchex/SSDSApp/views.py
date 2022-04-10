from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from SSDSApp.models import Brand

def MainView(request):
    bands = Brand.objects.all()
    return render(request, 'home.html', {'bands' :  bands})
