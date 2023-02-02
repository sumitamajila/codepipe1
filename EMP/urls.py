"""EMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from certification import views



urlpatterns = [
    path("admin/", admin.site.urls),
    # path("welcome/", views.welcome),
    # path("create/", views.create),
    # path("read/", views.read),
    # path("update/", views.update),
    # path("delete/", views.delete),
    path('certification/', include("certification.urls"))
 ]

