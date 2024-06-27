from rest_framework import mixins
from .common_response import NewResponse
__all__ = ['NewRetrieveMixin', 'NewListMixin', 'NewCreateMixin', 'NewUpdateMixin', 'NewDeleteMixin']


class NewListMixin(mixins.ListModelMixin):

    def list(self, request, *args, **kwargs):

        res = super(NewListMixin, self).list(request, *args, **kwargs)

        return NewResponse(message="查询已完成!", result=res.data)


class NewCreateMixin(mixins.CreateModelMixin):

    def create(self, request, *args, **kwargs):
        res = super(NewCreateMixin, self).create(request, *args, **kwargs)
        return NewResponse(message="新增已完成!")


class NewRetrieveMixin(mixins.RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        res = super(NewRetrieveMixin, self).retrieve(request, *args, **kwargs)
        return NewResponse(message="查询已完成!", result=res.data)


class NewUpdateMixin(mixins.UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        res = super(NewUpdateMixin, self).update(request, *args, **kwargs)
        return NewResponse(message="更新已完成!")


class NewDeleteMixin(mixins.DestroyModelMixin):

    def destroy(self, request, *args, **kwargs):
        res = super(NewDeleteMixin, self).destroy(request, *args, **kwargs)
        return NewResponse(message="删除已完成!", result=res.data)

    def perform_destroy(self, instance):
        """ 软删除 """
        instance.is_deleted = True
        instance.save()
