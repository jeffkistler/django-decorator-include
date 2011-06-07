from django.conf.urls.defaults import *
from django.http import HttpResponse

def deeply_nested(request):
    return HttpResponse('deeply nested!')

urlpatterns = patterns('',
    url(r'^deeply_nested/$', deeply_nested, name='deeply_nested'),
)
