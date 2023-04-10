from django.shortcuts import render
from formsapp.models import Employee
# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get('firstname') and request.POST.get('lastname'):
            emp_var = Employee()
            emp_var.first_name = request.POST.get('firstname')
            emp_var.last_name = request.POST.get('lastname')
            emp_var.save()
    return render(request,'index.html',{})
