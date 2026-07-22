from django.contrib import admin

from .models import Song, Album



@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "album_type",
        "release_date",
    )


    list_filter = (
        "album_type",
    )


    search_fields = (
        "name",
    )





@admin.register(Song)
class SongAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "album",
        "energy",
        "song_type",
    )


    list_filter = (
        "energy",
        "album",
        "song_type",
    )


    search_fields = (
        "title",
        "album__name",
        "vibe_tags",
        "mood_keywords",
    )


    fieldsets = (

        (
            "Información de la canción",
            {
                "fields": (
                    "title",
                    "album",
                    "song_type",
                    "energy",
                    "cover_image",
                )
            }
        ),


        (
            "Personalidad de Kimiko",
            {
                "fields": (
                    "vibe_tags",
                    "mood_keywords",
                    "kimiko_review",
                ),

                "description":
                "Define cómo Kimiko encontrará esta canción y cómo la recomendará."
            }
        ),


        (
            "Enlaces",
            {
                "fields": (
                    "youtube_url",
                    "spotify_url",
                )
            }
        ),

    )