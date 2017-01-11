from .models import Product
from common.views import basicPage

def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return basicPage(request, 'products/base_products.html', context)
