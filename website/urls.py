from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    #path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name ='logout'),
    path('register/', views.register, name ='register'),
    path('person/<int:pk>', views.customer_person, name ='person'),
    path('delete/<int:pk>', views.delete_customer, name ='delete'),
    path('Add_Record/', views.Add_Record, name ='Add_Record'),    
    path('update_record/<int:pk>', views.update_record, name ='update_record'),
]

