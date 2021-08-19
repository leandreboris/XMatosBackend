from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from Users.models import User
from Entities.models import Article

from .signals import  object_viewed_signal
from XMatosbackend.utils import get_client_ip


# Create your models here.


class ObjectViewed(models.Model):
    user            = models.CharField(max_length=30, blank=True, null=True)
    ip_address      = models.CharField(max_length=120, blank=True, null=True)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    article_id       = models.PositiveIntegerField()
    article_name = models.CharField(max_length=30)
    content_object  = GenericForeignKey('content_type', 'article_id')



    def __str__(self, ):
        return "{0} : {1} viewed at {2}".format(self.content_type, self.article_name,self.timestamp)


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
    article = Article.objects.get(id=instanceID)

    new_view_instance = ObjectViewed.objects.create(
                user=_user, 
                content_type=c_type,
                article_id=instanceID,
                article_name = article,
                ip_address=ip_address
                )

object_viewed_signal.connect(object_viewed_receiver)