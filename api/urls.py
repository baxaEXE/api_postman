from django.urls import path, include
from .views import custom_user,custom_user_detail,project,project_detail,task,task_detail


urlpatterns = [
    path('custom_user/',custom_user),
    path('custom_user_detail/<int:pk>/',custom_user_detail),
    path('project/',project),
    path('project_detail/<int:pk>/',project_detail),
    path('task/',task),
    path('task_detail/<int:pk>',task_detail),
    path('auth/', include('dj_rest_auth.urls')),
]