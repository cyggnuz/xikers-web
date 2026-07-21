from django.shortcuts import render, get_object_or_404
from .models import Member


def member_detail(request, pk=None):
    """
    Muestra el panel de detalle de UN integrante, junto con el sidebar
    que lista a todos los demas para poder cambiar de seleccion.

    Si no se pasa pk (ej: al entrar por primera vez a /members/),
    se muestra el primero de la lista segun display_order.
    """
    all_members = Member.objects.all()

    if pk:
        selected_member = get_object_or_404(Member, pk=pk)
    else:
        selected_member = all_members.first()

    context = {
        'all_members': all_members,
        'selected_member': selected_member,
    }
    return render(request, 'members/detail.html', context)