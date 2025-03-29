from django.middleware.base import BaseMiddleware

class MyNewMiddleware(BaseMiddleware):
    def __init__(self, get_response):
        super().__init__(get_response)

    def process_request(self, request):
        pass
