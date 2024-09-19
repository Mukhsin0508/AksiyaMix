from django.urls import path

from .views import *

urlpatterns = [
    path('create/', CustomUserListCreateView.as_view(), name='user_create'),
    path("user/<int:pk>/", CustomUserRetrieveUpdateDestroyView.as_view(), name="user"),

    path('create/', UserLocationListCreateView.as_view(), name='user_location_create'),
    path('user-location/<int:pk>/', UserLocationRetrieveUpdateDestroyView.as_view(), name="user_location"),

]