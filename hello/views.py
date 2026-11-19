from django.http import HttpResponse
from django.shortcuts import render


def hello_django(request):
    return HttpResponse('this is the page for this ')
def home(request):
    return render(request, 'hello/home.html')

def about(request):
    return render(request, 'hello/about.html')
    