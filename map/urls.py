from django.conf.urls import url

from . import views

app_name = 'map'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /map/temples/12.23/-4.222/0.532
    url(r'^temples/(?P<lat>[0-9.-]+)/(?P<lon>[0-9.-]+)/(?P<span>[0-9.-]+)$', views.temples, name='temples')
]