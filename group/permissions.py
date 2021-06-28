# from rest_framework.permissions import BasePermission
# from rest_framework.decorators import permission_classes

# def permission_required(perm):
#     def has_permission(self, request, view):

#         print("Somees")
#         return request.user.has_perm(perm)

#     Can = type(
#         'WrappedAPIView',
#         (BasePermission,),
#         {'message': 'You can not do ' + perm,
#         'has_permission': has_permission}
#     )
#     def decorator(func):
#         func.permission_classes = [Can]
#         return func
#     return decorator


from functools import wraps
from rest_framework.views import APIView

def has_permission(permission):
    def has_permission_decorator(func):
        @wraps(func)
        def has_permission_wrapper(*args, **kwargs):
            request = args[0].request
            if not request.user.has_perm(permission):
                return Response(status='Sorry User is not permitted')
            return func(*args, **kwargs)
        return has_permission_wrapper
    return has_permission_decorator


