from django.test import TestCase

# Create your tests here.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'better.settings')

import django
django.setup()

from src.Users.models import Users, Post, UserPosts, UserRoles


# pas = Users.create_password('123456')
# print(pas)
# user = Users.objects.create(username='any')
# user.set_password('123456')
# user.password = pas
# user.save()
# res = user.check_password('123456')
# print(res)

# post = Post.objects.create(name='董事长', desc='合伙人')
# print(post)

# obj = UserPosts.objects.create(user_id=1, post_id=1)
# print(obj)


res = [
        {
            "id": 1,
            "name": "工作空间",
            "path": "/workspace",
            "icon": "layui-icon-home",
            "children": [
                {
                    "id": 11,
                    "name": "工作台",
                    "path": "/workspace/workbench",
                    "icon": "layui-icon-util",
                    "children": []
                },
                {
                    "id": 12,
                    "name": "控制台",
                    "path": "/workspace/console",
                    "icon": "layui-icon-engine",
                    "children": []
                },
                {
                    "id": 13,
                    "name": "分析页",
                    "path": "/workspace/analysis",
                    "icon": "layui-icon-chart-screen",
                    "children": []
                },
                {
                    "id": 14,
                    "name": "监控页",
                    "path": "/workspace/monitor",
                    "icon": "layui-icon-find-fill",
                    "children": []
                }
            ]
        },
        {
            "id": 2,
            "name": "表单页面",
            "path": "/form",
            "icon": "layui-icon-table",
            "children": [
                {
                    "id": 15,
                    "name": "基础表单",
                    "path": "/form/base",
                    "icon": "layui-icon-form",
                    "children": []
                },
                {
                    "id": 16,
                    "name": "复杂表单",
                    "path": "/form/intricate",
                    "icon": "layui-icon-form",
                    "children": []
                },
                {
                    "id": 17,
                    "name": "分步表单",
                    "path": "/form/step",
                    "icon": "layui-icon-form",
                    "children": []
                }
            ]
        },
        {
            "id": 3,
            "name": "列表页面",
            "path": "/table",
            "icon": "layui-icon-align-left",
            "children": [
                {
                    "id": 18,
                    "name": "查询列表",
                    "path": "/table/base",
                    "icon": "layui-icon-search",
                    "children": []
                },
                {
                    "id": 19,
                    "name": "卡片列表",
                    "path": "/table/card",
                    "icon": "layui-icon-file-b",
                    "children": []
                },
                {
                    "id": 20,
                    "name": "项目列表",
                    "path": "/table/project",
                    "icon": "layui-icon-templeate-one",
                    "children": []
                },
                {
                    "id": 21,
                    "name": "文章列表",
                    "path": "/table/article",
                    "icon": "layui-icon-carousel",
                    "children": []
                }
            ]
        },
        {
            "id": 4,
            "name": "结果页面",
            "path": "/result",
            "icon": "layui-icon-template",
            "children": [
                {
                    "id": 22,
                    "name": "成功页面",
                    "path": "/result/success",
                    "icon": "layui-icon-success",
                    "children": []
                },
                {
                    "id": 23,
                    "name": "失败页面",
                    "path": "/result/failure",
                    "icon": "layui-icon-error",
                    "children": []
                }
            ]
        },
        {
            "id": 5,
            "name": "异常页面",
            "path": "/error",
            "icon": "layui-icon-unlink",
            "children": [
                {
                    "id": 24,
                    "name": "403",
                    "path": "/error/403",
                    "icon": "layui-icon-not-found",
                    "children": []
                },
                {
                    "id": 25,
                    "name": "404",
                    "path": "/error/404",
                    "icon": "layui-icon-not-found",
                    "children": []
                },
                {
                    "id": 26,
                    "name": "500",
                    "path": "/error/500",
                    "icon": "layui-icon-not-found",
                    "children": []
                }
            ]
        },
        {
            "id": 6,
            "name": "菜单嵌套",
            "path": "/menu",
            "icon": "layui-icon-app",
            "children": [
                {
                    "id": 27,
                    "name": "子目录",
                    "path": "/menu/menu1",
                    "icon": "layui-icon-component",
                    "children": [
                        {
                            "id": 41,
                            "name": "三级菜单",
                            "path": "/menu/menu1/menu1",
                            "icon": "layui-icon-template-one",
                            "children": []
                        },
                        {
                            "id": 42,
                            "name": "菜单三级",
                            "path": "/menu/menu1/menu2",
                            "icon": "layui-icon-template-one",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 28,
                    "name": "二级目录",
                    "path": "/menu/menu2",
                    "icon": "layui-icon-component",
                    "children": [
                        {
                            "id": 43,
                            "name": "子菜单",
                            "path": "/menu/menu2/menu1",
                            "icon": "layui-icon-template-one",
                            "children": []
                        },
                        {
                            "id": 44,
                            "name": "三级子菜单",
                            "path": "/menu/menu2/menu2",
                            "icon": "layui-icon-template-one",
                            "children": []
                        }
                    ]
                }
            ]
        },
        {
            "id": 7,
            "name": "内置指令",
            "path": "/directive",
            "icon": "layui-icon-test",
            "children": [
                {
                    "id": 29,
                    "name": "权限指令",
                    "path": "/directive/permission",
                    "icon": "layui-icon-template",
                    "children": []
                }
            ]
        },
        {
            "id": 8,
            "name": "外链页面",
            "path": "/page",
            "icon": "layui-icon-link",
            "children": [
                {
                    "id": 30,
                    "name": "原生跳转",
                    "path": "http://www.baidu.com",
                    "icon": "layui-icon-layouts",
                    "children": []
                }
            ]
        },
        {
            "id": 9,
            "name": "个人中心",
            "path": "/enrollee",
            "icon": "layui-icon-slider",
            "children": [
                {
                    "id": 31,
                    "name": "我的资料",
                    "path": "/enrollee/profile",
                    "icon": "layui-icon-username",
                    "children": []
                },
                {
                    "id": 32,
                    "name": "我的消息",
                    "path": "/enrollee/message",
                    "icon": "layui-icon-email",
                    "children": []
                }
            ]
        },
 ]


# def custom_dir(result):
#     def clean_children(item):
#         # 检查 'children' 是否存在且不为空
#         if 'children' in item and item['children']:
#             # 递归地清理 'children' 中的每个项，最多嵌套三层
#             item['children'] = [clean_children(child) for child in item['children']]
#         else:
#             # 如果 'children' 为空或不存在，从字典中删除它
#             item.pop('children', None)
#         return item
#
#     # 处理列表中的每个项
#     return [clean_children(item) for item in result]

# def custom_dir(result):
#     def clean_children(item, depth=3):
#         # 检查 'children' 是否存在且不为空，并且递归深度大于0
#         if 'children' in item and item['children'] and depth > 0:
#             # 清理 'children' 中的每个项，递归深度减1
#             item['children'] = [clean_children(child, depth - 1) for child in item['children']]
#         elif 'children' in item:
#             # 如果 'children' 为空或不存在，从字典中删除它
#             del item['children']
#
#         return item
#
#     # 使用循环来构建新列表，减少列表推导的使用
#     new_result = []
#     for item in result:
#         new_result.append(clean_children(item))
#
#     return new_result
#
# import json
# a = custom_dir(res)
# print(json.dumps(a, ensure_ascii=False))

UserRoles.objects.create(user_id=2, role_id=1)


