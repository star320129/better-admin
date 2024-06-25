import hashlib
from src.Perms import models as p_models
from src.Users import models as u_models


def token_cache_key(token):
    """
    为token生成hash值
    :param token:
    :return:
    """
    return hashlib.sha256(str(token).encode('utf-8')).hexdigest()


def permissions_user(user):
    """
    为权限校验提供权限列表
    :param user:
    :return:
    """
    roles_pk = roles_user(user)
    relation_queryset = p_models.RolePerms.objects.filter(role_id__in=roles_pk, is_deleted=False).all()

    permission_obj = []
    for rel in relation_queryset:
        permission_obj.append(p_models.Permission.objects.filter(pk=rel.id, is_deleted=False, elem=3).first())

    permissions = []
    for permission in permission_obj:
        permissions.append(permission.path)

    return permissions


def roles_user(user):

    roles_pk = [rel.role_id for rel in u_models.UserRoles.objects.filter(user_id=user.id, is_deleted=False).all()]
    # roles = [role for role in p_models.Role.objects.filter(pk__in=roles_pk).all()]
    return roles_pk


def init_queryset(user, elem):
    """
    根据角色为视图类提供权限的queryset对象
    :param user:
    :param elem:
    :return:
    """
    roles_pk = roles_user(user)
    if roles_pk:
        rel_queryset = p_models.RolePerms.objects.filter(role_id__in=roles_pk, is_deleted=False).all()
        perms = []
        for rel in rel_queryset:
            perms.append(rel.perms_id)
        perms_queryset = p_models.Permission.objects.filter(id__in=perms, elem=elem, is_deleted=False).all()
        return perms_queryset
