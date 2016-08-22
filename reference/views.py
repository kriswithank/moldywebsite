from common.views import basicPage

def index(request):
    return basicPage(request, 'reference/base_reference.html', {})
