#forms python file
from django import forms

class Employee_info(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()