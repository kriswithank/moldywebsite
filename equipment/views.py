from .models import Equipment
from common.views import basicPage

def index(request):
    context = {'equipment': Equipment.objects.all()}
    return basicPage(request, 'equipment/base_equipment.html', context)
