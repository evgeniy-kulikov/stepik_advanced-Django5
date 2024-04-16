from django.shortcuts import render
from hr.models import Employee


def homePageView(request):
    employees = Employee.objects.filter(about='Test')
    return render(request, 'hr/list.html', {'employees': employees})
