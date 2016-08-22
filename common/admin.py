from .models import BasicPost, TitledBasicPost, Image, NavMenuItem
from django import forms
from django.contrib import admin
from django.db import models

class NavMenuItemAdmin(admin.ModelAdmin):
    fields = ('position', 'display_text', 'reference_url_name')
    list_display = ('display_text', 'reference_url_name', 'position')
    list_display_links = None
    list_editable = ('display_text', 'reference_url_name', 'position')
    ordering = ['position', 'display_text']



class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class BasicPostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

class TitledBasicPostAdmin(admin.ModelAdmin):
    fields = ('title', 'body_markdown')
    inlines = [ImageInline]



admin.site.register(NavMenuItem, NavMenuItemAdmin)
admin.site.register(BasicPost, BasicPostAdmin)
admin.site.register(TitledBasicPost, TitledBasicPostAdmin)
