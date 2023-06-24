from django.urls import path
from crud import views


urlpatterns = [
    path("", views.principal, name="principal"),
    path("principal/", views.principal, name="principal"),
    path("navegacion/", views.navegacion, name="navegacion"),
    path("signup/", views.signup, name="signup"),
    path("sigin/", views.sigin, name="sigin"),
    path("logout/", views.signout, name="logout"),
    path("task/", views.task, name= "task"),
    path("task_delete/<int:id>/", views.task_delete, name= "task_delete"),
    path("new_task/", views.new_task, name="new_task"),
    
]