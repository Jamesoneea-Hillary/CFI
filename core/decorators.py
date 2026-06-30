from django.shortcuts import redirect

def role_required(role):
    def wrapper(view_func):
        def inner(request, *args, **kwargs):
            if request.user.role == role or request.user.role == "admin":
                return view_func(request, *args, **kwargs)
            return redirect('dashboard_home')
        return inner
    return wrapper