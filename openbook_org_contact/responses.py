from rest_framework.response import Response


class ApiMessageResponse(Response):
    """
    A generic API Response
    """

    def __init__(self, message, status=None, template_name=None, headers=None, content_type=None):
        super().__init__({'message': message}, status, template_name, headers, content_type)
