from rest_framework import generics

# Create your views here.
from .models import User
from .serializers import UserCreateSerializer
from rest_framework import permissions

# View All Users
class User(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]