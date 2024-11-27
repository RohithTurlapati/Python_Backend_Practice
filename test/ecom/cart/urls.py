from django.urls import path
from cart.views import UserListCreateAPIView


urlpatterns = [
    path("", UserListCreateAPIView.as_view()),
]