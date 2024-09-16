from tkinter.font import names

from django.urls import path

from .views import *

urlpatterns = [
    path('create/', CustomUserListCreateView.as_view(), name='user_create'),
    path("user/<int:pk>/", CustomUserRetrieveUpdateDestroyView.as_view(), name="user"),

    path('create/', UserLocationListCreateView.as_view(), name='user_location_create'),
    path('user-location/<int:pk>/', UserLocationRetrieveUpdateDestroyView.as_view(), name="user_location"),

    path("create/", UserTokenListCreateView.as_view(), name="user_token_create"),
    path("user-token/<int:pk>/", UserTokenRetrieveUpdateDestroyView.as_view(), name="user-token")

]