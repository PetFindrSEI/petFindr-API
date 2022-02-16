from rest_framework import generics

# Create your views here.
from .models import Pet
from .serializers import PetSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# View All Pets
class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Found View        
class PetListFound(generics.ListCreateAPIView):
    queryset = Pet.objects.all().filter(status='Found')
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Lost View
class PetListLost(generics.ListCreateAPIView):
    queryset = Pet.objects.all().filter(status='Lost')
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite create method
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Pet Detail
class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsOwnerOrReadOnly]