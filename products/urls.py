from . import views
from django.conf.urls import url

app_name = 'products'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_slug>[\w-]+)/$', views.detail, name='detail'),
]
