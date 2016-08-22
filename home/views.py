from common.views import basicPage

def index(request):
    return basicPage(request, 'home/base_home.html', {})
