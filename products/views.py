from .models import Product
from common.views import basicPage

def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return basicPage(request, 'products/base_products.html', context)


def detail(request, product_slug):
    context = {
        'product': Product.objects.get(slug=product_slug),
    }
    return basicPage(request, 'products/product_detail.html', context)
