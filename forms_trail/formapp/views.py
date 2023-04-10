from django.shortcuts import render
from .import forms
# Create your views here.
def empformview(request):
    form = forms.Employee_info()
    empinfo = {'empform':form}
    return render(request,'formapp/index.html',context=empinfo)