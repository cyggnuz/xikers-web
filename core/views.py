from django.shortcuts import render
from .models import Member  # Importamos el modelo de los integrantes

# views.py
# Vistas de la app core: la página de inicio y lo que sea compartido
# por todo el sitio (por ahora, solo el home).


def home(request):
    """Página de inicio: perfil básico del grupo y roster de integrantes."""
    # Obtenemos los integrantes activos ordenados
    members = Member.objects.filter(is_active=True).order_by('order')
    
    return render(request, 'core/home.html', {
        'members': members
    })