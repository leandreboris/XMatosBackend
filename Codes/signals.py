from django.db.models.signals import post_save
from django.dispatch import receiver
from Users.models import User
from .models import Code



@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created and instance.is_same_ip is False:
        Code.objects.create(user=instance)


