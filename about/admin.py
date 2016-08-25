from .models import AboutSection
from common.admin import PostImageInline
from django.contrib import admin

class AboutSectionAdmin(admin.ModelAdmin):
    fields = ['title', 'position', 'body_markdown']
    inlines = [PostImageInline]

admin.site.register(AboutSection, AboutSectionAdmin)
