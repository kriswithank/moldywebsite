from .models import Faq, FaqOld, FaqCategory
from django.contrib import admin

class FaqsOldInline(admin.StackedInline):
    model = FaqOld
    extra = 1
    ordering = ['position', 'question_text']

class FaqsInline(admin.StackedInline):
    model = Faq
    extra = 1
    ordering = ['position', 'title']
    fields = ['position', 'title', 'body_markdown']

class FaqCategoryAdmin(admin.ModelAdmin):
    fields = ('position', 'display_text')
    list_display = ('position', 'display_text')
    list_display_links = ('display_text',)
    list_editable = ('position',)
    inlines = [FaqsOldInline, FaqsInline]
    ordering = ['position', 'display_text']

admin.site.register(FaqCategory, FaqCategoryAdmin)
