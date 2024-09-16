from rest_framework import generics, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import *
from .serializers import *


# =========== CRUD for the CustomUser model ==========
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.object.all()
    serializers = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.object.all()
    serializers = CustomUserSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# ========== CRUD for the UserLocation model ==========
class UserLocationListCreateView(generics.ListCreateAPIView):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return  Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserLocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLocation.objects.all()
    serializer_class = CustomUserSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



# ========= CRUD for the UserToken model ==============
class UserTokenListCreateView(generics.ListCreateAPIView):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status.HTTP_400_BAD_REQUEST)

class UserTokenRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)