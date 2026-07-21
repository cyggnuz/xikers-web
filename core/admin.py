from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'role', 'is_active')
    
    # 🎯 Especificamos que el link para abrir el registro sea el NOMBRE, no el 'order'
    list_display_links = ('name',)
    
    # Ahora sí puedes editar 'order' e 'is_active' directamente desde la tabla
    list_editable = ('order', 'is_active')
    
    search_fields = ('name', 'role')