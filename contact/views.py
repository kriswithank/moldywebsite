from common.views import basicPage

def index(request):
    return basicPage(request, 'contact/base_contact.html', {})
