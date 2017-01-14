from .models import Equipment, EquipmentGalleryImage
from django.contrib import admin


class GalleryImageInline(admin.StackedInline):
    model = EquipmentGalleryImage
    extra = 1


class EquipmentAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline,]


admin.site.register(Equipment, EquipmentAdmin)
