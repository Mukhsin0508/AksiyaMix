from django.urls import path
from .views import *


urlpatterns = [

    path("create/", CompanyListCreateView.as_view(), name="company_create"),
    path("company/<int:pk>/", CompanyRetrieveUpdateDestroyView.as_view(), name="company"),

    path("create/", CompanyLocationListCreateView.as_view(), name='company_location_create'),
    path('company-locations/<int:pk>/', CompanyLocationRetrieveUpdateDestroyView.as_view(),
         name='company_location-detail'),

    path("create/", CompanyTimeTableListCreateView.as_view(), name="company_timetable_create"),
    path("company-timetable/<int:pk>/", CompanyTimeTableRetrieveUpdateDestroyView.as_view(), name="company_timetable"),


]