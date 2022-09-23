from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('thanks/',views.say_thanks,name='thanks'),
        path('my_egos/', views.list_user_egos, name='manage_egos_list'),
        path('create_ego/', views.get_ego, name='ego_create'),
        path('<pk>/edit/', views.update_ego, name='ego_edit'),
        path('<pk>/delete/', views.ego_delete, name='ego_delete'),
]
