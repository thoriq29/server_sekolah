from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from sekolah_kita_server.core.decorators import user_staff_required


def login_view(request):
    auth_form = AuthenticationForm(data=request.POST or None)
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        return redirect('backoffice:province:index')
    
    context_data = {
        'form': auth_form,
        'title': 'Login',
    }
    return render(request, 'backoffice/login.html', context_data)


def logout_view(request):
    logout(request)
    return redirect('backoffice:login_view')
