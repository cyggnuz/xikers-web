from django.shortcuts import render
from .models import Member
from music_bot.models import Song


def home(request):
    """Página de inicio: perfil básico del grupo y roster de integrantes."""

    members = Member.objects.filter(
        is_active=True
    ).order_by(
        'order'
    )

    songs = Song.objects.all().order_by(
        'album',
        'title'
    )

    return render(request, 'core/home.html', {
        'members': members,
        'songs': songs,
    })


def discography(request):
    """Sección de discografía."""

    songs = Song.objects.all().order_by(
        'album',
        'title'
    )

    return render(request, 'core/discography.html', {
        'songs': songs,
    })