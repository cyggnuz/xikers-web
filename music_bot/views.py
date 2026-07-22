import random

from django.http import JsonResponse
from django.db.models import Q

from .models import Song



# Traducción de palabras humanas a tags internos
MOOD_MAP = {

    "feliz": [
        "feliz",
        "alegre",
        "divertido",
        "brillante",
        "positivo"
    ],

    "triste": [
        "emocional",
        "melancolico",
        "tranquilo",
        "suave"
    ],

    "energia": [
        "energia",
        "potente",
        "intenso",
        "motivador"
    ],

    "bailar": [
        "baile",
        "dance",
        "performance",
        "coreografia"
    ],

    "oscuro": [
        "oscuro",
        "dark",
        "misterioso",
        "intenso"
    ],

    "relajado": [
        "tranquilo",
        "chill",
        "calmado",
        "comfort"
    ],

    "epico": [
        "epico",
        "cinematico",
        "grande",
        "poderoso"
    ]

}



def recommend_song(request):

    energy = request.GET.get("energy")
    vibe = request.GET.get("vibe")


    # Carga canciones junto a su álbum relacionado
    songs = Song.objects.select_related(
        "album"
    ).all()



    # Filtrar por energía
    if energy:

        songs = songs.filter(
            energy=energy
        )



    # Buscar por emoción / texto
    if vibe:

        vibe = vibe.lower()


        keywords = MOOD_MAP.get(
            vibe,
            [vibe]
        )


        query = Q()


        for word in keywords:

            query |= Q(
                vibe_tags__icontains=word
            )

            query |= Q(
                mood_keywords__icontains=word
            )


        songs = songs.filter(query)



    # Si no encontró coincidencias,
    # usa toda la discografía
    if not songs.exists():

        songs = Song.objects.select_related(
            "album"
        ).all()



    # Si no existen canciones
    if not songs.exists():

        return JsonResponse({

            "success": False,

            "message":
            "🐱 Aún no tengo canciones registradas en mi Tricky House."

        })



    # Escoger máximo 3 canciones aleatorias
    songs_list = list(songs)


    random.shuffle(
        songs_list
    )


    recommendations = songs_list[:3]



    return JsonResponse({

        "success": True,

        "songs": [

            {

                "title": song.title,


                # Ahora obtiene el nombre del álbum relacionado
                "album":
                song.album.name
                if song.album
                else "",


                "energy":
                song.get_energy_display(),


                "review":
                song.kimiko_review,


                "youtube_url":
                song.youtube_url or "",


                "spotify_url":
                song.spotify_url or "",


                "cover_url":
                song.cover_image.url
                if song.cover_image
                else ""

            }

            for song in recommendations

        ]

    })