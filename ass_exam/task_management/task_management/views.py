from django.shortcuts import render
from taskmodel.models import task_model
def homepage(request):
    
    data = task_model.objects.all()
    return render(request,'base.html',{'data':data})




