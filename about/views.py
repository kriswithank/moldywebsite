from common.views import basicPage
from .models import AboutSection

def index(request):
    context = {
        'sections': AboutSection.objects.all()
    }
    return basicPage(request, 'about/base_about.html', context)
