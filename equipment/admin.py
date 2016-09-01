from .models import Equipment, EquipmentGalleryImage, EquipmentLongDescription
from common.models import BasicPost
from django.contrib import admin


class GalleryImageInline(admin.StackedInline):
    model = EquipmentGalleryImage
    extra = 1

class LongDescriptionInline(admin.StackedInline):
    model = EquipmentLongDescription
    fields = ['body_markdown']
    max_num = 1


class EquipmentAdmin(admin.ModelAdmin):
    inlines = [LongDescriptionInline, GalleryImageInline]


admin.site.register(Equipment, EquipmentAdmin)
