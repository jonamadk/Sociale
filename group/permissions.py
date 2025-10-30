
from django.http import HttpResponse, HttpRequest, request
from functools import wraps
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied

from rest_framework.permissions import DjangoModelPermissions

def has_permission(permission):
    def has_permission_decorator(func):
        @wraps(func)
        def has_permission_wrapper(*args, **kwargs):
            request = args[0].request
            if not request.user.has_perm(permission):
                raise PermissionDenied
            return func(*args, **kwargs)
        return has_permission_wrapper
    return has_permission_decorator


