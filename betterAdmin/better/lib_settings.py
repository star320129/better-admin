"""
celery配置
Email配置
Websocket配置
sentry
"""
import sentry_sdk

# Broker配置，使用Redis作为消息中间件
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
# BACKEND配置，使用redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_ACCEPT_CONTENT = ['pickle']
CELERY_TASK_SERIALIZER = 'pickle'
# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'pickle'
# 任务结果过期时间，秒
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 时区配置
CELERY_TIMEZONE = 'Asia/Shanghai'

# celery_beat 定时任务
# CELERY_BEAT_SCHEDULE = {
#     'update-user-task': {
#             'task': 'apps.user.tasks.update_user_list',
#             # 'schedule': timedelta(seconds=5),   # 每隔5秒钟，更新user_list
#             'schedule': timedelta(minutes=5),   # 每隔5分钟，更新user_list
#             'args': (),
#         },
# }

# 启动celery：
#     celery -A better worker -l debug -P eventlet

# 启动beat：
#     celery -A better beat -l debug

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'star_320129@qq.com'  # 帐号
EMAIL_HOST_PASSWORD = 'eqrjxphblaqrbada'  # 密码
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = False  # 禁用TLS
EMAIL_USE_SSL = True  # 启用SSL加密

# websocket
CHANNEL_LAYERS = {
    "default": {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': ["redis://localhost:6379/3"],
            # 'hosts': ["redis://60.204.238.150:6379/3"],
        },
    }
}


# sentry
sentry_sdk.init(
    dsn="https://efff8bd977691d0e30ede72a007874b2@o4507513503219712.ingest.us.sentry.io/4507513614172160",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
