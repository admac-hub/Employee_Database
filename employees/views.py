from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee


# Create your views here.
def employee_detail(request , pk):
        employee = Employee.objects.get(pk=pk)
        context = {
                'employee' : employee
        }
        return render(request, 'employee_detail.html', context)