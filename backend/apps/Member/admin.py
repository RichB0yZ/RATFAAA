from django.contrib import admin

from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass
    # list_display = ('date','full_name','mobile', 'unit', 'status', 'document_approved')
    # list_display_links = ['full_name']
    # list_editable  = ['document_approved',]
    # list_filter = ('unit',)