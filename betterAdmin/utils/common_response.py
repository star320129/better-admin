from rest_framework.response import Response


class NewResponse(Response):

    def __init__(self, message, status=200, **kwargs):
        self.status = status
        self.message = message

        data = {
            'status': self.status,
            'message': self.message,
        }
        if kwargs:
            data.update(kwargs)

        super().__init__(data=data, status=status, **kwargs)

