from .models import Product, ProductGalleryImage
from django.contrib import admin



class ProductGalleryImageInline(admin.StackedInline):
    model = ProductGalleryImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fields = ['position', 'name', 'slug', 'completion_date', 'short_desc', 'markdown', 'thumbnail']
    inlines = [ProductGalleryImageInline,]


admin.site.register(Product, ProductAdmin)
