from django.contrib import admin
from django.urls import path
from managementapp import views

urlpatterns = [
    path('',views.home),
    path('master/',views.master),
    path('display/',views.display),
    path('addmission/',views.addmission),
    path('update/<id>/',views.update),
    path('delete/<id>/',views.delete),
]