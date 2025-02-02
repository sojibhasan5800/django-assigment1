from django.shortcuts import render,redirect
from .forms import task_form
from .models import task_model
from django.db import connection

# Create your views here.
def taskpage(request):
  
    if request.method == 'POST':
        user_form = task_form(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('home_page')
    
    else:
        user_form = task_form()
        return render(request,'add_catagory.html',{'form':user_form})
    

def editpost(request,id):
   postdata = task_model.objects.get(pk=id)
   post_forms = task_form(instance=postdata)
   print(post_forms)
   if request.method == 'POST':
         post_forms =  task_form(request.POST,instance=postdata)
         if post_forms.is_valid():
            postdata.is_completed=True
            post_forms.save()
            return redirect("home_page")
         
   return render(request, 'add_task.html', {'form' : post_forms})
              
def deletepost(request,id):
    delete_data = task_model.objects.get(pk=id)
    delete_data.delete()
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM taskmodel_task_model) WHERE name = 'taskmodel_task_model'")
    return redirect("home_page")

