from rest_framework import generics

# Create your views here.
from .models import Pet
from .serializers import PetSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsOwnerOrReadOnly]