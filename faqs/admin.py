from .models import FaqOld, FaqCategory
from django.contrib import admin

class FaqsOldInline(admin.StackedInline):
    model = FaqOld
    extra = 1
    ordering = ['position', 'question_text']

class FaqCategoryAdmin(admin.ModelAdmin):
    fields = ('position', 'display_text')
    list_display = ('position', 'display_text')
    list_display_links = ('display_text',)
    list_editable = ('position',)
    inlines = [FaqsOldInline]
    ordering = ['position', 'display_text']

admin.site.register(FaqCategory, FaqCategoryAdmin)
