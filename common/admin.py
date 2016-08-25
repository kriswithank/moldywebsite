from .models import BasicPost, TitledBasicPost, PostImage, NavMenuItem
from django.contrib import admin

class NavMenuItemAdmin(admin.ModelAdmin):
    fields = ('position', 'display_text', 'reference_url_name')
    list_display = ('display_text', 'reference_url_name', 'position')
    list_display_links = None
    list_editable = ('display_text', 'reference_url_name', 'position')
    ordering = ['position', 'display_text']



class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class BasicPostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

class TitledBasicPostAdmin(admin.ModelAdmin):
    fields = ('title', 'body_markdown')
    inlines = [PostImageInline]



admin.site.register(NavMenuItem, NavMenuItemAdmin)
admin.site.register(BasicPost, BasicPostAdmin)
admin.site.register(TitledBasicPost, TitledBasicPostAdmin)
