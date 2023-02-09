from django.urls import path
from . import views

#those imports that are below are for seeing imgs in the admin panel
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.main, name='main'),
    path('search',views.searchinf, name='search')
]

#img in the admin panel
urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)