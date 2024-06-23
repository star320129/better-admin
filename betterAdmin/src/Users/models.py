from django.db import models
from utils import NewModel
from src.Perms.models import Role
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.


class Users(NewModel):

    USERNAME_FIELD = 'username'
    _gender = ((0, 'female'), (1, 'male'), (2, 'Unknown'))

    username = models.CharField(max_length=64, unique=True, null=True, blank=True, verbose_name='Username')
    password = models.CharField(max_length=255, null=True, blank=True, verbose_name='Password')
    gender = models.PositiveSmallIntegerField(choices=_gender, default=1, verbose_name='Gender')
    email = models.CharField(max_length=64, blank=True, null=True, unique=True, verbose_name="Email")
    phone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="Phone Number")
    avatar = models.ImageField(upload_to='avatar', default='avatar/luck.jpg')

    is_active = models.BooleanField(default=True, verbose_name='Is Active?')
    is_superuser = models.BooleanField(default=False, verbose_name='Is Superuser?')

    @staticmethod
    def _create_password(password, salt=None, hasher="default"):
        return make_password(password, salt=salt, hasher=hasher)

    def set_password(self, password):
        self.password = self._create_password(password)

    def check_password(self, password):
        return check_password(password, self.password)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'better_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name


class OnlineUser(NewModel):

    addr = models.CharField(max_length=128, verbose_name='Login Addr', blank=True, null=True)
    browser = models.CharField(max_length=255, verbose_name='Browser', blank=True, null=True)
    ip = models.CharField(max_length=64, verbose_name='IP', blank=True, null=True)
    token = models.CharField(max_length=255, verbose_name='Token', blank=True, null=True)

    user = models.ForeignKey(
        to='Users',
        related_name='online',
        on_delete=models.PROTECT,
        db_constraint=False,
        verbose_name='One to Many for User',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'better_online_user'
        verbose_name = 'Online User'
        verbose_name_plural = verbose_name


class Post(NewModel):

    name = models.CharField(max_length=64, verbose_name='Name')
    desc = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'better_post'
        verbose_name = 'Post'
        verbose_name_plural = verbose_name


class UserRoles(NewModel):

    user = models.ForeignKey(
        to='Users',
        on_delete=models.PROTECT,
        db_constraint=False,
        verbose_name='User',
        null=True,
        blank=True
    )

    role = models.ForeignKey(
        to=Role,
        on_delete=models.PROTECT,
        db_constraint=False,
        verbose_name='Role',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'better_user_roles'
        verbose_name = 'User Roles'
        verbose_name_plural = verbose_name


class UserPosts(NewModel):

    user = models.ForeignKey(
        to='Users',
        db_constraint=False,
        verbose_name='User',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    post = models.ForeignKey(
        to='Post',
        db_constraint=False,
        verbose_name='Post',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'better_user_posts'
        verbose_name = 'User Posts'
        verbose_name_plural = verbose_name
