from celery import shared_task
from django.core.cache import cache
from . import models
from celery import Task
from django.core.mail import send_mail
from django.conf import settings


class SendEmailTask(Task):

    def on_success(self, retval, task_id, args, kwargs):
        info = f'任务id: {task_id}, 参数是: {args}, 执行成功 !'
        send_mail('celery任务监控成功报告', info, settings.EMAIL_HOST_USER, ["star_320129@sina.com", ])

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        info = f'任务失败-- 任务id: {task_id}, 参数为: {args}, 失败 ! 失败信息为: {exc}'
        send_mail('celery任务监控失败告警', info, settings.EMAIL_HOST_USER, ["star_320129@sina.com", ])


@shared_task
def update_user_queryset():
    """
    更新缓存
    :return:
    """
    cache.delete('user_queryset')
    user_list = models.Users.objects.filter(is_deleted=False).all()
    cache.set('user_queryset', user_list, timeout=3600)


@shared_task(base=SendEmailTask)
def send_email(msg, email):
    send_mail(
        subject="明星集团",
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
