from django.contrib import admin
from .models import AboutSection, AboutSectionOld
from common.admin import ImageInline

class AboutSectionAdmin(admin.ModelAdmin):
    fields = ['title', 'position', 'body_markdown']
    inlines = [ImageInline]

admin.site.register(AboutSectionOld)
admin.site.register(AboutSection, AboutSectionAdmin)
