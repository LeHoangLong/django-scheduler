import threading
from django.http import request
import django.core.exceptions as exceptions


THREAD_LOCAL = threading.local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: request.HttpRequest):
        if request.path.startswith('/admin'):
            return self.get_response(request)
        tenant = request.headers.get('x-tenant')
        if tenant is None:
            tenant = request.get_host()
        setattr(THREAD_LOCAL, "TENANT", tenant)
        response = self.get_response(request)
        return response


def get_tenant() -> str:
    tenant = getattr(THREAD_LOCAL, "TENANT", None)
    if tenant is None:
        raise exceptions.BadRequest("missing tenant")
    return tenant
