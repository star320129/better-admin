from rest_framework.filters import BaseFilterBackend


class UserFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        username = request.query_params.get('userName')
        gender = request.query_params.get('gender')
        phone = request.query_params.get('phone')

        if username:
            return queryset.filter(username__contains=username).all()

        if gender:
            return queryset.filter(gender=gender).all()

        if phone:
            return queryset.filter(phone=phone).all()

        return queryset
