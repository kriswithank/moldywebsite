from common.views import basicPage

def index(request):
    return basicPage(request, 'equipment/base_equipment.html', {})
