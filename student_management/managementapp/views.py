from django.shortcuts import render
from managementapp.models import student
# Create your views here.
def home(request):
    return render(request,'managementapp/homepage.html')

def master(request):
    return render(request,'managementapp/master.html')

def display(request):
    obj=student.objects.all()
    context={
        'data':obj
    }
    return render(request,'managementapp/display.html',context)

def addmission(request):
    if request.method=='POST':
        n=request.POST.get('name')
        c=request.POST.get('city')
        p=request.POST.get('percentage')
        mob=request.POST.get('contact')
        e=request.POST.get('email')
        cl=request.POST.get('clg')
        d=request.POST.get('degree')
        y=request.POST.get('year')
        co=request.POST.get('course')
        x=student(name=n,city=c,percentage=p,contact=mob,email=e,college=cl,degree=d,year=y,course=co)
        x.save()
    return render(request,'managementapp/addmission.html')

def update(request,id):
    obj2=student.objects.get(id=id)
    context={
        'data2':obj2
    }
    if request.method=='POST':
        n=request.POST.get('name')
        c=request.POST.get('city')
        p=request.POST.get('percentage')
        mob=request.POST.get('contact')
        e=request.POST.get('email')
        cl=request.POST.get('clg')
        d=request.POST.get('degree')
        y=request.POST.get('year')
        co=request.POST.get('course')

        obj2.name=n
        obj2.city=c
        obj2.percentage=p
        obj2.contact=mob
        obj2.email=e
        obj2.clg=cl
        obj2.degree=d
        obj2.year=y
        obj2.course=co

        obj2.save()


    return render(request,'managementapp/update.html',context)

def delete(request,id):
    obj3=student.objects.get(id=id)
    obj3.delete()
    return render(request,'managementapp/display.html')