from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'), # as_view() linka uma classe de view a uma URL
    path("users/create", views.create_user, name='create_user'),
    path("users/list", views.list_user, name='list_user'),
    path("users/list/<int:pk>", views.retrieve_user, name='retrieve_user'),
    path("users/update/<int:pk>", views.update_user, name='update_user'),
    path("users/delete/<int:pk>", views.delete_user, name='delete_user'),
]
