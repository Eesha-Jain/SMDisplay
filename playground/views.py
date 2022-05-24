from django.shortcuts import render
from django.http import HttpResponse

from .functions import fetchdata

# Create your views here.
def say_hello(request):
    data = fetchdata.getData()
    return render(request, 'index.html', {'data': data})
