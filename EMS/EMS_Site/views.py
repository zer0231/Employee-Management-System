from django.http import Http404
from django.shortcuts import render
from .models import employee_detail,job

# Create your views here.
def home(request):
    employees = employee_detail.objects.all()
    return render(request,"home.html",{'title':'employee management system','employees':employees})

def e_detail(request,e_id):
    try:
        employee = employee_detail.objects.get(id=e_id)
    except employee_detail.DoesNotExist:
        raise Http404("Employee Not Found")
    return render(request,"employee_detail.html",{"title":"Employee name"})