import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'better.settings')

import django
django.setup()

from src.Perms import models

from django.db import transaction


@transaction.atomic
def init():

    perms_list = [
        {'path': '/workspace', 'icon': 'layui-icon-home', 'name': '工作空间'},
        {'path': '/form', 'icon': 'layui-icon-table', 'name': '表单页面'},
        {'path': '/table', 'icon': 'layui-icon-align-left', 'name': '列表页面'},
        {'path': '/result', 'icon': 'layui-icon-template', 'name': '结果页面'},
        {'path': '/error', 'icon': 'layui-icon-unlink', 'name': '异常页面'},
        {'path': '/menu', 'icon': 'layui-icon-app', 'name': '菜单嵌套'},
        {'path': '/directive', 'icon': 'layui-icon-test', 'name': '内置指令'},
        {'path': '/page', 'icon': 'layui-icon-link', 'name': '外链页面'},
        {'path': '/enrollee', 'icon': 'layui-icon-slider', 'name': '个人中心'},
        {'path': '/system', 'icon': 'layui-icon-set', 'name': '系统管理'},
    ]

    obj_list = [models.Permission(**perm) for perm in perms_list]

    models.Permission.objects.bulk_create(obj_list)

# init()


@transaction.atomic
def sub_init():

    perms_list = [
        {'path': '/workspace/workbench', 'icon': 'layui-icon-util', 'name': '工作台', 'elem': 2, 'parent_id': 1},
        {'path': '/workspace/console', 'icon': 'layui-icon-engine', 'name': '控制台', 'elem': 2, 'parent_id': 1},
        {'path': '/workspace/analysis', 'icon': 'layui-icon-chart-screen', 'name': '分析页', 'elem': 2, 'parent_id': 1},
        {'path': '/workspace/monitor', 'icon': 'layui-icon-find-fill', 'name': '监控页', 'elem': 2, 'parent_id': 1},
        {'path': '/form/base', 'icon': 'layui-icon-form', 'name': '基础表单', 'elem': 2, 'parent_id': 2},
        {'path': '/form/intricate', 'icon': 'layui-icon-form', 'name': '复杂表单', 'elem': 2, 'parent_id': 2},
        {'path': '/form/step', 'icon': 'layui-icon-form', 'name': '分步表单', 'elem': 2, 'parent_id': 2},
        {'path': '/table/base', 'icon': 'layui-icon-search', 'name': '查询列表', 'elem': 2, 'parent_id': 3},
        {'path': '/table/card', 'icon': 'layui-icon-file-b', 'name': '卡片列表', 'elem': 2, 'parent_id': 3},
        {'path': '/table/project', 'icon': 'layui-icon-templeate-one', 'name': '项目列表', 'elem': 2, 'parent_id': 3},
        {'path': '/table/article', 'icon': 'layui-icon-carousel', 'name': '文章列表', 'elem': 2, 'parent_id': 3},
        {'path': '/result/success', 'icon': 'layui-icon-success', 'name': '成功页面', 'elem': 2, 'parent_id': 4},
        {'path': '/result/failure', 'icon': 'layui-icon-error', 'name': '失败页面', 'elem': 2, 'parent_id': 4},
        {'path': '/error/403', 'icon': 'layui-icon-not-found', 'name': '403', 'elem': 2, 'parent_id': 5},
        {'path': '/error/404', 'icon': 'layui-icon-not-found', 'name': '404', 'elem': 2, 'parent_id': 5},
        {'path': '/error/500', 'icon': 'layui-icon-not-found', 'name': '500', 'elem': 2, 'parent_id': 5},
        {'path': '/menu/menu1', 'icon': 'layui-icon-component', 'name': '子目录', 'elem': 1, 'parent_id': 6},
        {'path': '/menu/menu2', 'icon': 'layui-icon-component', 'name': '二级目录', 'elem': 1, 'parent_id': 6},
        {'path': '/directive/permission', 'icon': 'layui-icon-template', 'name': '权限指令', 'elem': 2, 'parent_id': 7},
        {'path': 'http://www.baidu.com', 'icon': 'layui-icon-layouts', 'name': '原生跳转', 'elem': 2, 'parent_id': 8},
        {'path': '/enrollee/profile', 'icon': 'layui-icon-username', 'name': '我的资料', 'elem': 2, 'parent_id': 9},
        {'path': '/enrollee/message', 'icon': 'layui-icon-email', 'name': '我的消息', 'elem': 2, 'parent_id': 9},
        {'path': '/system/user', 'icon': 'layui-icon-user', 'name': '用户管理', 'elem': 2, 'parent_id': 10},
        {'path': '/system/role', 'icon': 'layui-icon-user', 'name': '角色管理', 'elem': 2, 'parent_id': 10},
        {'path': '/system/menu', 'icon': 'layui-icon-spread-left', 'name': '菜单管理', 'elem': 2, 'parent_id': 10},
        {'path': '/system/organization', 'icon': 'layui-icon-transfer', 'name': '机构管理', 'elem': 2, 'parent_id': 10},
        {'path': '/system/dictionary', 'icon': 'layui-icon-read', 'name': '字典管理', 'elem': 2, 'parent_id': 10},
        {'path': '/system/file', 'icon': 'layui-icon-file', 'name': '文件管理', 'elem': 2, 'parent_id': 10},
        {'path': '/system/login', 'icon': 'layui-icon-date', 'name': '登录日志', 'elem': 2, 'parent_id': 10},
        {'path': '/system/option', 'icon': 'layui-icon-survey', 'name': '操作日志', 'elem': 2, 'parent_id': 10},

    ]

    obj_list = [models.Permission(**perm) for perm in perms_list]

    models.Permission.objects.bulk_create(obj_list)

# sub_init()


@transaction.atomic
def subs_init():

    perms_list = [
        {'path': '/menu/menu1/menu1', 'icon': 'layui-icon-template-one', 'name': '三级菜单', 'elem': 2, 'parent_id': 27},
        {'path': '/menu/menu1/menu2', 'icon': 'layui-icon-template-one', 'name': '菜单三级', 'elem': 2, 'parent_id': 27},
        {'path': '/menu/menu2/menu1', 'icon': 'layui-icon-template-one', 'name': '子菜单', 'elem': 2, 'parent_id': 28},
        {'path': '/menu/menu2/menu2', 'icon': 'layui-icon-template-one', 'name': '三级子菜单', 'elem': 2, 'parent_id': 28},
    ]
    obj_list = [models.Permission(**perm) for perm in perms_list]

    models.Permission.objects.bulk_create(obj_list)


# subs_init()


@transaction.atomic
def button():

    perms_list = [
        {'path': 'user:action:create', 'name': '添加用户', 'elem': 3},
        {'path': 'user:action:update', 'name': '编辑用户', 'elem': 3},
        {'path': 'user:action:delete', 'name': '删除用户', 'elem': 3},
        {'path': 'user:action:list', 'name': '用户列表', 'elem': 3},
        {'path': 'user:export', 'name': '用户导出', 'elem': 3},
        {'path': 'user:import', 'name': '用户导入', 'elem': 3},
    ]
    obj_list = [models.Permission(**perm) for perm in perms_list]

    models.Permission.objects.bulk_create(obj_list)


# button()

# role = models.Role.objects.create(name='测试一号')
# print(role)


@transaction.atomic
def role_perms():
    perms_list = [10, 33, 45, 46, 47, 48, 49, 50]

    obj_list = [models.RolePerms(role_id=1, perms_id=perm) for perm in perms_list]
    models.RolePerms.objects.bulk_create(obj_list)


# role_perms()
