from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import InstanceCheckMeta
from Entities.models import Categorie, Article

from .signals import  object_viewed_signal
from XMatosbackend.utils import get_client_ip


# Create your models here.
class ArticlesViewed(models.Model):
    username       = models.CharField(max_length=30, blank=True, null=True)
    user_IP_address      = models.CharField(max_length=120, blank=True, null=True)
    content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    article_id       = models.PositiveIntegerField()
    article_name = models.CharField(max_length=30, blank=True, null=True)
    article_category = models.CharField(max_length=256,blank=True, null=True)
    content_object  = GenericForeignKey('content_type', 'article_id')
    article_provider = models.CharField(max_length=30,blank=True, null=True)


    def __str__(self, ):
        return "{0} : {1} viewed at {2}".format(self.article_category, self.article_name,self.timestamp)


    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Article viewed'
        verbose_name_plural = 'Articles viewed'



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


    # Count and check whether it is empty or not
    article_results = Article.objects.filter(id=instanceID).count()
    if article_results == 1:
        article = Article.objects.get(id=instanceID)
        article.views += 1
        article.save()
        provider = article.provider
        _category = Categorie.objects.get(libelle=article.category)
        category = _category.libelle
    

    new_view_instance = ArticlesViewed.objects.create(
                username=_user, 
                content_type=c_type,
                article_id=instanceID,
                article_name = article,
                user_IP_address=ip_address,
                article_category = category,
                article_provider = provider
                )

object_viewed_signal.connect(object_viewed_receiver)