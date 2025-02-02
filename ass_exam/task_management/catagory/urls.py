
from django.urls import path
from .views import catagorypage

urlpatterns = [

    path('catagorys',catagorypage,name='catagory_page')   
]