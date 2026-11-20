from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'hello/home.html')
@login_required
def about(request):
    return render(request, 'hello/about.html')
