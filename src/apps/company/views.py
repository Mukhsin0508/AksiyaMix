from rest_framework import generics
from .models import Company , CompanyLocation, CompanyTimeTable
from .serializers import CompanySerializer, CompanyLocationSerializer, CompanyTimeTableSerializer



# =============== CRUD for the Company model ================
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()

    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()

    serializer_class = CompanySerializer



# =============== CRUD for the CompanyLocation model ================
class CompanyLocationListCreateView(generics.ListCreateAPIView):
    queryset = CompanyLocation.objects.all()

    serializer_class = CompanyLocationSerializer

class CompanyLocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyLocation.objects.all()

    serializer_class = CompanyLocationSerializer



# =============== CRUD for the CompanyTimeTable model ================
class CompanyTimeTableListCreateView(generics.ListCreateAPIView):
    queryset = CompanyTimeTable.objects.all()

    serializer_class = CompanyTimeTableSerializer

class CompanyTimeTableRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyTimeTable.objects.all()

    serializer_class = CompanyTimeTableSerializer