from .models import MarkdownImage, MarkdownModel
from django.contrib import admin



class MarkdownImageInline(admin.TabularInline):
    model = MarkdownImage
    extra = 1



class MarkdownModelAdmin(admin.ModelAdmin):
    inlines = [MarkdownImageInline,]



admin.site.register(MarkdownModel, MarkdownModelAdmin)
