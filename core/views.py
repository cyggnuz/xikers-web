from django.shortcuts import render

# Create your views here.
# views.py
# Vistas de la app core: la página de inicio y lo que sea compartido
# por todo el sitio (por ahora, solo el home).


def home(request):
    """Página de inicio: perfil básico del grupo (sección 1 del proyecto)."""
    return render(request, 'core/home.html')