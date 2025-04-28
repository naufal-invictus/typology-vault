from django.contrib import admin
from .models import PDFDocument, Tag

class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploader_name', 'upload_date', 'accuracy_score')
    list_filter = ('tags',)
    search_fields = ('title', 'uploader_name')
    filter_horizontal = ('tags',)

admin.site.register(Tag)

try:
    admin.site.unregister(PDFDocument)
except admin.sites.NotRegistered:
    pass

admin.site.register(PDFDocument, PDFDocumentAdmin)
