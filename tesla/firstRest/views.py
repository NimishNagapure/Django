from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from firstRest.models import Employee
from firstRest.models import Department


# Create your views here.

def employee(request):
    #     emp = {
    #     'id': 1,
    #     'name':'Nimish',
    #     'branch':'IT'
    #     }

    data = Employee.objects.select_related().all()
    response = {"employee": list(data.values('id', 'name', 'branch'))}
    return JsonResponse(response)

    # newdata = Department.objects.all()
    # newresponce = {"department ": list(newdata.values('emp', 'emp_id', 'id', 'name'))}
    # return JsonResponse(newresponce)
