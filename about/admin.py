from .models import AboutSection
from common.admin import MarkdownImageInline
from django.contrib import admin

class AboutSectionAdmin(admin.ModelAdmin):
    fields = ['title', 'position', 'markdown']
    inlines = [MarkdownImageInline,]

admin.site.register(AboutSection, AboutSectionAdmin)
