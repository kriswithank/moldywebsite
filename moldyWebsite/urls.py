from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('home:index'), permanent=False)),
    url(r'^about/', include('about.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^equipment/', include('equipment.urls')),
    url(r'^faqs/', include('faqs.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^reference/', include('reference.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#######
# IMPORTANT!!!!!
# Once in production, remove the + static(...) bit, it is unsafe.
