from django.db import models
from utils import NewModel
# Create your models here.


class Role(NewModel):

    name = models.CharField(max_length=32, unique=True, blank=True, null=True, verbose_name='Name')
    level = models.PositiveSmallIntegerField(default=1, blank=True, null=True, verbose_name='Level')
    state = models.BooleanField(default=True, blank=True, null=True, verbose_name='IS Active')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'better_role'
        verbose_name = 'Role'
        verbose_name_plural = verbose_name


class Permission(NewModel):

    _type = ((0, 'directory'), (1, 'sub_dir'), (2, 'menu'), (3, 'button'))

    name = models.CharField(max_length=64, unique=True, blank=True, null=True, verbose_name='Name')
    path = models.CharField(max_length=128, unique=True, blank=True, null=True, verbose_name='PS: Path')
    elem = models.PositiveSmallIntegerField(choices=_type, default=0, blank=True, verbose_name='Type')
    icon = models.CharField(max_length=255, blank=True, null=True, verbose_name='Icon')

    is_extra_link = models.BooleanField(default=False, blank=True, null=True, verbose_name='IS Extra Link')

    parent = models.ForeignKey(
        'self',
        db_constraint=False,
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.PROTECT,
        verbose_name='Parent'
    )

    def type_name(self):
        return self.get_elem_display()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'better_permission'
        verbose_name = 'Permission'
        verbose_name_plural = verbose_name


class RolePerms(NewModel):

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        verbose_name='Role',
        blank=True,
        null=True,
        db_constraint=False,
    )

    perms = models.ForeignKey(
        Permission,
        on_delete=models.PROTECT,
        verbose_name='Permissions',
        blank=True,
        null=True,
        db_constraint=False,
    )

    class Meta:
        db_table = 'better_role_perms'
        verbose_name = 'Role Permissions'
        verbose_name_plural = verbose_name
