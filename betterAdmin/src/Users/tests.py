from django.test import TestCase

# Create your tests here.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'better.settings')

import django
django.setup()

from src.Users.models import Users, Post, UserPosts


# pas = Users.create_password('123456')
# print(pas)
# user = Users.objects.filter(username='admin').first()
# user.set_password('123456')
# user.password = pas
# user.save()
# res = user.check_password('123456')
# print(res)

# post = Post.objects.create(name='董事长', desc='合伙人')
# print(post)

# obj = UserPosts.objects.create(user_id=1, post_id=1)
# print(obj)


