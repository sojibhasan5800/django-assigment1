
from django.urls import path
from .views import taskpage

urlpatterns = [

    path('taskmodel',taskpage,name='task_page')   
]