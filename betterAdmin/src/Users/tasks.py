from celery import shared_task
from django.core.cache import cache
from . import models


@shared_task
def update_user_queryset():
    """
    更新缓存
    :return:
    """
    cache.delete('user_queryset')
    user_list = models.Users.objects.filter(is_deleted=False).all()
    cache.set('user_queryset', user_list, timeout=3600)

