from django.urls import path

from . import views

urlpatterns = [
    path("thanks/", views.say_thanks, name="thanks"),
    path("my_egos/", views.list_user_egos, name="list_egos"),
    path("create_ego/", views.create_ego, name="create_ego"),
    path("<pk>/edit/", views.edit_ego, name="edit_ego"),
    path("<pk>/delete/", views.delete_ego, name="delete_ego"),
    path("list_morphs/", views.list_morphs, name="list_morphs"),
]
