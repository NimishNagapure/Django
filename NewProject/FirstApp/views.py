from django.shortcuts import render
from django.http import JsonResponse
from FirstApp.models import Employee

# Create your views here.
def employee(request):
    # emp = {
    #     'id': 1,
    #     'name':'Nimish',
    #     'branch':'IT'
    #     }

    data = Employee.objects.all()
    response = {"employee": list(data.values('id','name', 'salary'))}
    return JsonResponse(response)
