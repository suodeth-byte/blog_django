from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.get_all_permissions)
            return redirect('home')

        else:
            return view_func(request, *args, **kwargs)
    return wrapper
