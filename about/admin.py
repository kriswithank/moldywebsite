from .models import AboutSection
from common.admin import ImageInline
from django.contrib import admin

class AboutSectionAdmin(admin.ModelAdmin):
    fields = ['title', 'position', 'body_markdown']
    inlines = [ImageInline]

admin.site.register(AboutSection, AboutSectionAdmin)
