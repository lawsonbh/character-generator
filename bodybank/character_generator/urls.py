from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('ego/',views.get_ego,name='ego'),
        path('thanks/',views.say_thanks,name='thanks'),
        path('my_egos/', views.ManageEgoListView.as_view(), name='manage_egos_list'),
        path('create_ego/', views.EgoCreateView.as_view(), name='ego_create'),
        path('<pk>/edit/', views.EgoUpdateView.as_view(), name='ego_edit'),
        path('<pk>/delete/', views.EgoDeleteView.as_view(), name='ego_delete')
]
