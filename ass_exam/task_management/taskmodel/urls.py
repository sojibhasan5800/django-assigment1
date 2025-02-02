
from django.urls import path
from .views import taskpage,editpost,deletepost

urlpatterns = [

    path('taskmodel',taskpage,name='task_page'),  
    path('editpost/<int:id>/',editpost,name='edit_page'),  
    path('deletepost/<int:id>/',deletepost,name='delete_page'),  
]