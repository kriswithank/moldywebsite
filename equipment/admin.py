from .models import Equipment, EquipmentGalleryImage
from django.contrib import admin


class GalleryImageInline(admin.StackedInline):
    model = EquipmentGalleryImage
    extra = 1


class EquipmentAdmin(admin.ModelAdmin):
    fields = ['position', 'name', 'short_desc', 'markdown', 'thumbnail']
    inlines = [GalleryImageInline,]


admin.site.register(Equipment, EquipmentAdmin)
