from django.urls import path
from .views import IndexView, CreateUserView

urlpatterns = [
    path("", IndexView.as_view(), name='index'), # as_view() is used to link the class-based view into the URL
    path("users/", CreateUserView.as_view(), name='user_list'),  # Example for a user list view
]
