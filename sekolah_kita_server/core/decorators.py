from functools import wraps

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def user_staff_required(view_func):
    @wraps(view_func)
    def _check_user_account(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)

        messages.info(request, 'Please login as a staff')
        return redirect(reverse('backoffice:login_view'))
    return _check_user_account
