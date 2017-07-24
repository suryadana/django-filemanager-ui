from django.conf.urls import url
from filemanager import views

urlpatterns = [
    url(r'^basic/$', 
        views.basic, 
        name='filemanager-basic'
    ),
    url(r'^connector/$',
    	views.connector,
    	name='filemanager-connector'
    ),

]