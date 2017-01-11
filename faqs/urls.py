from . import views
from django.conf.urls import url

app_name = 'faqs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
