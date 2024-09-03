from django.urls import path
from .views import home, TaskList,TaskDetail,TaskUpdate,TaskCreate,TaskDelete

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/create/', TaskCreate.as_view(),name='task-create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(),name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(),name='task-delete'),
    
]