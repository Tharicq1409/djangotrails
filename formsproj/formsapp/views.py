from django.shortcuts import render
from formsapp.models import Employee
# Create your views here.
def index(request):
    if request.method == "POST":   #if it is a POST Method then ...
        if request.POST.get('firstname') and request.POST.get('lastname'):  #if the values are present then it gets user input
            emp_var = Employee() #creating object for Employee model
            emp_var.first_name = request.POST.get('firstname')  #----|-->sending user input to Employee Model
            emp_var.last_name = request.POST.get('lastname')  #-----|
            emp_var.save()   #saving datas to model
        return render(request,'success.html',{})      #Display success message Page
    return render(request,'index.html',{})            #user Input Page
