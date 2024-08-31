from django.shortcuts import render
from functools import wraps


def user_has_permission(permission):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.has_perm(permission):
                return render(request, '404.html', status=404)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator           
