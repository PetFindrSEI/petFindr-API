from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.PetList.as_view(), name='pet_list'),
    path('pets/<int:pk>', views.PetDetail.as_view(), name='pet_detail')
]