from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from about.views import index as about_index
from contact.views import index as contact_index
from equipment.views import index as equipment_index
from faqs.views import index as faqs_idex
from home.views import index as home_index
from reference.views import index as reference_index

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('home'), permanent=False)),
    url(r'^about/$', about_index, name='about'),
    url(r'^contact/$', contact_index, name='contact'),
    url(r'^equipment/$', equipment_index, name='equipment'),
    url(r'^faqs/$', faqs_idex, name='faqs'),
    url(r'^home/$', home_index, name='home'),
    url(r'^products/', include('products.urls')),
    url(r'^reference/$', reference_index, name='reference'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#######
# IMPORTANT!!!!!
# Once in production, remove the + static(...) bit, it is unsafe.
