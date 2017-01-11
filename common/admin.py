from .models import BasicPost, TitledBasicPost, PostImage
from django.contrib import admin



class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1



class BasicPostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]



class TitledBasicPostAdmin(admin.ModelAdmin):
    fields = ('title', 'body_markdown')
    inlines = [PostImageInline]



admin.site.register(BasicPost, BasicPostAdmin)
admin.site.register(TitledBasicPost, TitledBasicPostAdmin)
