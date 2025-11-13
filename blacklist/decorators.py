from functools import wraps
from django.utils.decorators import available_attrs

def public_api_view(view_func):
    """
    Decorator to mark a view as public and bypass ESI authentication.
    """
    def _wrapped_view(request, *args, **kwargs):
        request.esi_is_public = True
        return view_func(request, *args, **kwargs)
    return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)
