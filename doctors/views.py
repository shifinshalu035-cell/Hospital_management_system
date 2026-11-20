from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm
from django.contrib.auth.decorators import login_required

@login_required
def doctor_list(request):
    query = request.GET.get('q', '')
    if query:
        doctors = Doctor.objects.filter(name__icontains=query) | Doctor.objects.filter(specialization__icontains=query)
    else:
        doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors, 'query': query})
@login_required
def doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_form.html', {'form': form})
@login_required
def doctor_edit(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {'form': form})
@login_required
def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})