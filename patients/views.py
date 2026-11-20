from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm

# 1. List all patients (with search)
def patient_list(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(name__icontains=query)
    else:
        patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients, 'query': query})

# 2. Show one patient
def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

# 3. Add a new patient
def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})

# 4. Edit a patient
def patient_edit(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})

# 5. Delete a patient
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})