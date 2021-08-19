from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def about(request):
    return render(request, 'hospital/about.html')

def Contact(request):
    return render(request, 'hospital/contact.html')

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0
    p = 0
    a = 0
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1

    d1 = {'d':d, 'p':p, 'a':a}
    return render(request, 'hospital/index.html', d1)

def Login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "Yes"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, 'hospital/login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    context = {
        'doc':doc
    }
    return render(request, 'hospital/view_doctor.html', context)

def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n, mobile=c, specialist=sp)
            error = "no"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, 'hospital/add_doctor.html', d)

def Delete_Doctor(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('view_doctor')

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    context = {
        'pat':pat
    }
    return render(request, 'hospital/view_patient.html', context)

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=='POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a)
            error = "no"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, 'hospital/add_patient.html', d)

def Delete_Patient(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('view_patient')

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    context = {
        'appoint':appoint
    }
    return render(request, 'hospital/view_appointment.html', context)

def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t1 = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t1)
            error = "no"
        except:
            error = "Yes"
    d = {'error': error, 'doctor':doctor1, 'patient':patient1 }
    return render(request, 'hospital/add_appointment.html', d)

def Delete_Appointment(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('view_appointment')



    


