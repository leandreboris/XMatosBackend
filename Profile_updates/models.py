# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from rest_framework.response import Response


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "127.0.0.1{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    send_mail(
        "Password Reset for {title}".format(title="XMATOS"),
        email_plaintext_message,
        'xservicenoreply@gmail.com',
        [reset_password_token.user.email],
    )
    return Response(reset_password_token.key)