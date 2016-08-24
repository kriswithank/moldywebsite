from .models import FaqOld, FaqCategory
from common.views import basicPage

def index(request):
    faq_categories = []
    for category in FaqCategory.objects.all():
        faq_categories.append({
            'display_text': category.display_text,
            'faqs': FaqOld.objects.filter(category__display_text=category.display_text)
            })
    context = {
        'faq_categories': faq_categories
    }
    return basicPage(request, 'faqs/base_faq.html', context)
