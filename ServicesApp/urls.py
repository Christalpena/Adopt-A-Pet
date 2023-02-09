from django.urls import path 
from ServicesApp import views

urlpatterns= [
    path('',views.services,name="services"),
    path('<int:id>',views.modal,name='form')
]