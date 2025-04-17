from django.http import HttpResponseForbidden
from functools import wraps
from django.contrib import messages
from django.shortcuts import render, redirect

def role_required(allowed_roles=[]):

    def decorator(view_func):

        @wraps(view_func)

        def _wrapped_view(request, *args, **kwargs):

            if request.user.is_authenticated and request.user.groups.exists():

                user_role = request.user.groups.all()[0].name

                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)

                else:
                    return render(request, 'forbidden.html', {
                        'message': 'You do not have permission to access this page.',
                        'redirect_url': 'home-page-view',
                        'type' : 'forbidden'
                    }, status=403)

            return render(request, 'forbidden.html', {
                'message': 'You must login to continue.',
                'redirect_url': 'home-page-view',
                'type' : 'not_logged_in'
            }, status=403)

        return _wrapped_view

    return decorator