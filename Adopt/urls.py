from django.urls import path
from . import views

urlpatterns=[
    path('',views.adopt, name='adopt'),
    path('Information/<int:id>',views.informationPage, name= 'infpage'),
    path('form/<int:id>',views.adoptform, name="adoptform"),
    path('dogs',views.dogs,name='dog'),
    path('cats',views.cats,name='cat'),

]