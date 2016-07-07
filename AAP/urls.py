from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from table import views

admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.redirect2main, name='redirect'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^p/results/$', views.send_data_permission, name='send_data_permission'),
    url(r'^a/results/$', views.send_data_ad, name='send_data_ad'),
    url(r'^o/results/$', views.send_data_obf, name='send_data_obf'),
    url(r'^m/results/$', views.send_data_minsdk, name='send_data_minsdk'),

    url(r'^main/$', views.index, name='index'),
    url(r'^permission/$', views.index_p, name='index_p'),
    url(r'^adsdk/$', views.index_a, name='index_a'),
    url(r'^minreqsdk/$', views.index_m, name='index_m'),
    url(r'^obfuscation/$', views.index_o, name='index_o'),

    url(r'^upload/$', views.uploader, name='uploader'),
    url(r"^(?P<md5>\w+)/show/$", views.show, name='show'),
    # url(r'report.$', views.redirect2main, name='redirect'),
    # url(r'^report/', include('table.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)
