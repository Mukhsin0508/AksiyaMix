from django.urls import path
from .views import *


urlpatterns = [
    path('create/', DiscountTypesListCreateView.as_view(), name='discount_create'),
    path("discount-types/<int:pk>/", DiscountTypesRetrieveUpdateDestroyView.as_view(), name="discount_types"),

    path('create/', DiscountListCreateView.as_view(), name='discount_create'),
    path("discount/<int:pk>/", DiscountRetrieveUpdateDestroyView.as_view(), name="discount"),

]