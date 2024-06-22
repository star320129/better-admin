from rest_framework.response import Response


class NewResponse(Response):

    def __init__(self, message, status=200, **kwargs):
        self.status = status
        self.message = message

        data = {
            'status': self.status,
            'message': self.message,
        }

        assert isinstance(kwargs, dict), 'kwargs must be a dict!'

        data.update(kwargs)

        super().__init__(data=data, status=status)

