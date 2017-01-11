from .models import Product, ProductGalleryImage
from django.contrib import admin



class ProductGalleryImageInline(admin.StackedInline):
    model = ProductGalleryImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductGalleryImageInline,]


admin.site.register(Product, ProductAdmin)
