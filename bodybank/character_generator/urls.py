from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('ego/',views.get_ego,name='build-ego'),
        path('thanks/',views.say_thanks,name='thanks')
]
