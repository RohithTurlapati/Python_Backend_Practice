from rest_framework.generics import ListCreateAPIView
from cart.models import User
from cart.serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer