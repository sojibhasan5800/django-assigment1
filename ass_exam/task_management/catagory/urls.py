
from django.urls import path
from .views import catagorypage

urlpatterns = [

    path('catagory',catagorypage,name='catagory_page')   
]