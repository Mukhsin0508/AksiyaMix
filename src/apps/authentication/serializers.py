import os
import secrets
from os import access

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.core.cache import  cache
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.validators import phone_validate
from apps.authentication.sms_providers import EskizUz
from apps.user.validators import password_validate




# ========== Forgot Password Serializers ===================
class ForgotPasswordSerializer(serializers.Serializer):
    """
    Serializer for handling forgot password requests.
    It validates the username (phone number), generates a password reset token,
    and sends the reset link via SMS to the user.
    """
    username = serializers.CharField( validators = [phone_validate] )

    def validate_username(self , username):
        """
        Ensure the username exists in the database.
        Raises an error if the user is not found.
        """
        if not get_user_model().objects.filter( username = username ).exists( ):
            raise ValidationError( "User with this phone number does not exist" )
        return username

    def save(self , **kwargs):
        """
        Generates a password reset link and sends it to the user's phone via SMS.
        """
        username = self.validated_data['username']
        user = get_user_model().objects.get( username = username )

        # Use Django's built-in PasswordResetTokenGenerator
        token_generator = PasswordResetTokenGenerator()
        reset_token = token_generator.make_token( user )

        # Build the password reset URL
        reset_url = f"{os.environ['PASSWORD_RESET_BASE_URL']}/{reset_token}"
        reset_url = self.context['request'].build_absolute_uri( f'/reset-password/{user.pk}/{reset_token}/' )

        try:
            EskizUz.send_sms(
                username = username,
                message_type = 'FORGOT_PASSWORD',
                link = reset_url
            )
            return {"success": True, "message": "Password reset link sent successfully"}
        except Exception as e:
            print( f"Error sending SMS: {str ( e )}" )
            raise serializers.ValidationError( "Failed to send password reset link. Please try again later." )


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for handling password reset after receiving a reset link.
    It validates the password and ensures the new password and confirm password fields match.
    """
    password = serializers.CharField ( validators = [password_validate] , write_only = True )
    confirm_password = serializers.CharField ( write_only = True)
    refresh = serializers.CharField ( read_only = True )
    access = serializers.CharField ( read_only = True )

    def validate(self, attrs):
        """
        Ensure that the password and confirm password fields match.
        """
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match! ")

        return attrs



# ========== AUTH_CODE Verification Serializers ============
class VerifyCodeSerializer(serializers.Serializer):
    """
    Serializer for verifying the authentication code (AUTH_CODE) sent to the user upon registration.
    Ensures the user-provided code matches the code stored in the cache.
    """
    username = serializers.CharField(validators = [phone_validate])
    code = serializers.IntegerField()

    def validate(self, attrs):
        """
        Ensure the provided code matches the one sent to the user, which is stored in the cache.
        Raises an error if the codes don't match.
        """
        attrs = super().validate(attrs)
        username, code = attrs['username'], attrs['code']

        if cache.get(EskizUz.AUTH_CODE_KEY.format(username = username)) != code:
            raise  ValidationError(f"Code doesn't match, check the code we sent to {username}. ")


        return  attrs



# ========= Register (signup) Serializer ===================
class RegisterSerializer(VerifyCodeSerializer):
    """
    Serializer for handling user registration.
    Extends the VerifyCodeSerializer to include password validation and user creation.
    Once the user is verified, it generates JWT tokens (refresh and access) and deletes the auth code.
    """
    password = serializers.CharField( validators = [password_validate], write_only = True)
    refresh = serializers.CharField( read_only = True)
    access = serializers.CharField( read_only = True )

    def validate(self, attrs):
        """
        Validate the username and password, create a new user, and generate JWT tokens.
        """
        attrs = super().validate(attrs)

        username, password = attrs['username'], attrs['password']

        user = get_user_model().objects.create(username = username, password = password)

        cache.delete(EskizUz.AUTH_CODE_MESSAGE.format(username = username))

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)

        return attrs



class SendCodeSerializer(serializers.Serializer):
    username = serializers.CharField(validators = [phone_validate])

    def validate_username(self, username):
        if get_user_model().objects.filter(username = username).exists():
            raise ValidationError("User with this phone number already exists.")
        return username

    def save(self, *args, **kwargs):
        """
        Send registration code to the username
        :param args:
        :param kwargs: username
        :return: None
        """
        EskizUz.send_sms (
            message_type = "AUTH_CODE" ,
            username = self.validated_data['username'] ,
        )
















