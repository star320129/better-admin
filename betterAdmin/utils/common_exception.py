from django.core.exceptions import BadRequest, SuspiciousOperation
from django.http import Http404

from .common_response import NewResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.views import exception_handler
from loguru import logger


def record_log(request, exc, view=None):
    ip = request.META.get('REMOTE_ADDR')
    path = request.get_full_path()
    method = request.method
    user_id = request.user.id or 'AnonymousUser'

    detail = str(exc)

    if view:
        message = f"操作出错：{detail}, ip地址为：{ip}, 请求方式是：{method}，请求地址是：{path}，用户为：{user_id}, 视图类为: {view}"
    else:
        message = f"操作出错：{detail}, ip地址为：{ip}, 请求方式是：{method}，请求地址是：{path}，用户为：{user_id}"

    logger.add(
        sink='logs/exception.log',
        level='ERROR',
        format='{time:YYYY-MM-DD at HH:mm:ss}|{level}|{message}',
        colorize=True,
        rotation="5 MB",
        serialize=True,
        enqueue=True,
    )

    logger.error(message)


class CommonExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        for error in self.exception_dict():
            if isinstance(exception, self.exception_dict().get(error)[0]):
                record_log(request, exception)
                return NewResponse(message=error, status=self.exception_dict().get(error)[1])

    @staticmethod
    def exception_dict():
        match_dic = {
            '请求页面不存在': (Http404, 404),
            '请求格式不正确或数据无效': (BadRequest, 405),
            '检测到可疑操作': (SuspiciousOperation, 406),
        }
        return match_dic


def new_exception_handler(exc, content):

    drf_exception_handler = exception_handler(exc, content)

    if drf_exception_handler is not None:
        record_log(content.get('request'), exc, content.get('view'))
        return NewResponse(message=drf_exception_handler.data.get('detail', "The system is busy now !"), status=drf_exception_handler.status_code)

    return None
