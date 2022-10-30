from django.urls import path

from . import views

urlpatterns = [
    path("thanks/", views.say_thanks, name="thanks"),
    path("my_egos/", views.list_user_egos, name="list_egos"),
    path("create_ego/", views.create_ego, name="create_ego"),
    path("<pk>/edit_ego/", views.edit_ego, name="edit_ego"),
    path("<pk>/delete_ego/", views.delete_ego, name="delete_ego"),
    path("list_morphs/", views.list_morphs, name="list_morphs"),
    path(
        "my_character_sheets/",
        views.list_user_character_sheets,
        name="list_character_sheets",
    ),
    path(
        "create_character_sheet/",
        views.create_character_sheet,
        name="create_character_sheet",
    ),
    path(
        "<pk>/edit_character_sheet/",
        views.edit_character_sheet,
        name="edit_character_sheet",
    ),
    path(
        "<pk>/delete_character_sheet/",
        views.delete_character_sheet,
        name="delete_character_sheet",
    ),
]
