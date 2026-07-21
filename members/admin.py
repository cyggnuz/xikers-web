from django.contrib import admin
from .models import Member


    
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'position', 'age', 'favorite_color', 'display_order')
    list_editable = ('display_order',)
    ordering = ('display_order',)    