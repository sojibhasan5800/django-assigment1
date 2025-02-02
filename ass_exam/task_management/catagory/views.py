from django.shortcuts import render,redirect
from .forms import catagory_form
# Create your views here.
def catagorypage(request):
    if request.method == 'POST':
        cat_form = catagory_form(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('home_page')

    cat_form = catagory_form()
    return render(request,'add_catagory.html',{'form':cat_form})
