from django.shortcuts import render,redirect
from .forms import task_form

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
