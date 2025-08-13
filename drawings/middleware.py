import time
from django.db.utils import OperationalError


class WarmUpMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        for _ in range(5):
            try:
                return self.get_response(request)
            except OperationalError:
                time.sleep(1)
        return self.get_response(request)
