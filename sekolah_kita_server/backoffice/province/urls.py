from django.conf.urls import url 
from .views import index, details, add_province, edit_province

app_name = 'province'

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^(?P<id>\d+)$', details, name='details'),
    url(r'^(?P<id>\d+)$', details, name='details'),
    url(r'^add_province/$', add_province, name='add_province'),
    url(r'^(?P<id>\d+)/edit_province/$', edit_province, name='edit_province'),
]
