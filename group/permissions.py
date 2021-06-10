from rest_framework.permissions import BasePermission
from rest_framework.decorators import permission_classes

def permission_required(perm):
    def has_permission(self, request, view):

        print("Somees")
        return request.user.has_perm(perm)
    Can = type(
        'WrappedAPIView',
        (BasePermission,),
        {'message': 'You can not do ' + perm,
        'has_permission': has_permission}
    )
    def decorator(func):
        func.permission_classes = [Can]
        return func
    return decorator


