
from django.urls import path
from certification import views

urlpatterns = [

    path('welcome.html', views.welcome, name="welcome"),
    path('create/', views.create, name="create"),
    path('read/', views.read, name="read"),
    path('update/<id>', views.update, name="update"),
    path('delete/<id>', views.delete,name="delete"),

 ]
