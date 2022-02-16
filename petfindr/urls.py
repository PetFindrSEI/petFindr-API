from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.PetList.as_view(), name='pet_list'),
    path('pets/found/', views.PetListFound.as_view(), name='pet_list_found'),
    path('pets/lost/', views.PetListLost.as_view(), name='pet_list_lost'),
    path('pets/<int:pk>', views.PetDetail.as_view(), name='pet_detail')
]