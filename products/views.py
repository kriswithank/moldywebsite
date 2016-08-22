from common.views import basicPage

def index(request):
    return basicPage(request, 'products/base_products.html', {})
