from django.shortcuts import render,redirect


# Create your views here.
from .models import Doctor


def index(request):
    doctor = Doctor.objects.all()
    context= {
        'doctor' : doctor
    }
    return render(request,'home.html',context)

def addDoctor (request):
    name=request.GET['doctorname']
    specialist=request.GET['specialist']
    contact=request.GET['contact']
    age=request.GET['age']
    newDoctor= Doctor(dname=name,dspecialist=specialist,dcontact=contact,dage=age)
    newDoctor.save()
    return redirect('/')

def delete(request,id):
    doctor = Doctor.objects.get(pk=id)
    doctor.delete()
    return redirect('/')