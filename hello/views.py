from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

def home(request):
    context = {
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'appointment_count': Appointment.objects.count(),
        'scheduled_count': Appointment.objects.filter(status='Scheduled').count(),
    }
    return render(request, 'hello/home.html', context)

def about(request):
    return render(request, 'hello/about.html')