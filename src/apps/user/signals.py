from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.user.models import CustomUser
from django.core.mail import send_mail

# Signal Receiver: post_save signal when a new CustomUser instance is created
@receiver(post_save, sender=CustomUser)
def user_registered_handler(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)

# email sending function
def send_welcome_email(user):
    if user.email:
        send_mail(
            'Welcome!',
            'Thank you for registering.',
            'muxsinmuxtorov01@gmail.com',
            [user.email],
            fail_silently=False,
        )
    else:
        send_sms(user)  # Fallback to sending an SMS if no email is found

# SMS sending function (hypothetical)
def send_sms(user):
    # Actual SMS sending logic
    phone_number = user.phone_number
    # Playmobile.send_sms(phone_number, 'Welcome! Thank you for registering. Here is your discount code: ABC123')
    print(f"Sending SMS to {phone_number}")
