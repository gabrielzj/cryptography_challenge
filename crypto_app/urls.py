from django.urls import path
from .views import IndexView, CreateUserView, ListUserView, RetrieveUserView, UpdateUserView, DeleteUserView
urlpatterns = [
    path("", IndexView.as_view(), name='index'), # as_view() linka uma classe de view a uma URL
    path("users/create", CreateUserView.as_view(), name='create_user'),
    path("users/list", ListUserView.as_view(), name='list_user'),
    path("users/<int:pk>/retrieve", RetrieveUserView.as_view(), name='retrieve_user'),
    path("users/<int:pk>/update", UpdateUserView.as_view(), name='update_user'),
    path("users/<int:pk>/delete", DeleteUserView.as_view(), name='delete_user'),
]
