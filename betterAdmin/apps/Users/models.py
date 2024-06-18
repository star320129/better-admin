from django.db import models
from utils import NewModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(AbstractUser, NewModel):
    """
    用户表
    """

    _gender = ((0, 'female'), (1, 'male'), (2, 'Unknown'))
    gender = models.PositiveSmallIntegerField(choices=_gender, default=1, verbose_name='Gender')
    email = models.CharField(max_length=64, blank=False, null=False, unique=True, verbose_name="Email")
    phone = models.CharField(max_length=11, blank=False, null=False, unique=True, verbose_name="Phone Number")
    avatar = models.ImageField(upload_to='avatar', default='avatar/luck.jpg')
    created_at = super().date_joined

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'better_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class OnlineUser(NewModel):
    """
    在线用户表
    """

    addr = models.CharField(max_length=64, verbose_name='在线用户登录地址', blank=True, null=True)
    browser = models.CharField(max_length=128, verbose_name='浏览器', blank=True, null=True)
    ip = models.CharField(max_length=64, verbose_name='用户登录ip', blank=True, null=True)
    token = models.CharField(max_length=255, verbose_name='存用户token', blank=True, null=True)
    # 关联
    user = models.ForeignKey(
        to='User',
        related_name='online',
        on_delete=models.PROTECT,
        db_constraint=False,
        verbose_name='和用户的一对多',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'better_online_user'
        verbose_name = '在线用户的记录表'
        verbose_name_plural = verbose_name
