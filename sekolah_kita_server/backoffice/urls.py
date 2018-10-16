from django.conf.urls import url, include
from django.conf import settings
from .views import login_view, logout_view


app_name = 'backoffice'

urlpatterns = [
    url(r'^$', login_view, name='login_view'),
    #url(r'^login$', login_view, name='login_view'),
    url(r'^logout$', logout_view, name='logout_view'),
    url(r'^dashboard/', include('sekolah_kita_server.backoffice.province.urls')),
]