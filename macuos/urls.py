from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from.import views
import logging 

logging.getLogger('command').debug(' >>> ' + __name__)

urlpatterns = [ 
    # 2018/08/16 M00002 s-hama>>>
    #url(r'^', views.PostIndexView.as_view(), name='index'),
    path('', views.PostIndexView.as_view(), name='index'), 
    # 2018/08/16 M00002 s-hama <<<

    url(r'^detail/(?P<pk>[0-9]+)/$',
        views.PostDetailView.as_view(), name='detail'),
 
    url(r'^category/(?P<big>\w+)/(?P<small>\w+)/$',
        views.CategoryView.as_view(), name='category'),
 
    url(r'^category/(?P<big>\w+)/$',
        views.CategoryView.as_view(), name='category'),
 
    url(r'^tag/(?P<tag>\w+)/$', 
        views.TagView.as_view(), name='tag'),

    url(r'^profile/$',
        views.ProfileView.as_view(), name='profile'),

    url(r'^contact/$',
        views.ContactView.as_view(), name='contact'),

    url(r'^ppolicy/$',
        views.PpolicyView.as_view(), name='ppolicy'),

    url(r'^ads.txt',
	lambda x: HttpResponse('google.com, pub-4029756773390765, DIRECT, f08c47fec0942fa0', content_type='text/plain'), name='adsfile'),
]
