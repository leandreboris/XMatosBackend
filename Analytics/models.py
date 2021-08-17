from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from Users.models import User
from .signals import  object_viewed_signal
from XMatosbackend.utils import get_client_ip


# Create your models here.


class ObjectViewed(models.Model):
    user            = models.CharField(max_length=30, blank=True, null=True)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id       = models.PositiveIntegerField()
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    content_object  = GenericForeignKey('content_type', 'object_id')
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self, ):
        return "{0} viewed at {1}".format(self.content_object, self.timestamp)


    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'





def object_viewed_receiver(sender, instanceID, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    ip_address = None
    try:
        ip_address = get_client_ip(request)
    except:
        pass
    if request.user is None :
        _user = None
    else :
        _user = request.user

    new_view_instance = ObjectViewed.objects.create(
                user=_user, 
                content_type=c_type,
                object_id=instanceID,
                ip_address=ip_address
                )

object_viewed_signal.connect(object_viewed_receiver)