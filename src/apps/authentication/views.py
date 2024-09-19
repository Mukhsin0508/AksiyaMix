from lib2to3.fixes.fix_input import context
from logging import raiseExceptions

from future.utils import raise_
from rest_framework import generics, status
from rest_framework.generics import CreateAPIView , GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from urllib3 import request

from .models import *
from .serializers import *



class ForgotPasswordAPIView(CreateAPIView):
    """

    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = ForgotPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data, context={'request': request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'message': 'Link sent to your phone number successfully'}, status = status.HTTP_200_OK)


class PasswordResetConfirmAPIView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = PasswordResetSerializer

    def post(self, request, user_id, token, *args, **kwargs):
        serializer = self.serializer_class( data = request.data )
        serializer.is_valid( raise_exception = True )

        new_password = serializer.validated_data[ "new_password" ]

        try:
            user = get_user_model().objects.get(pk=user_id)
        except:
            raise ValidationError("Invalid user")

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            raise ValidationError("Invalid or expired token")

        user.set_password(new_password)
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Password has been reset successfully!",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        },
            status = status.HTTP_200_OK)




class SendCodeAPIView(GenericAPIView):
    """

    """
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status = 200)


class VerifyCodeAPIView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status = 200)


class RegisterAPIView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status = 200)





