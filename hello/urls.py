from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_django, name='hello_django'),
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
]
