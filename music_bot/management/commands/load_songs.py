import json
import os

from django.core.management.base import BaseCommand
from music_bot.models import Song, Album


class Command(BaseCommand):

    help = "Carga canciones desde songs.json"


    def handle(self, *args, **kwargs):

        file_path = os.path.join(
            "music_bot",
            "data",
            "songs.json"
        )


        if not os.path.exists(file_path):

            self.stdout.write(
                self.style.ERROR(
                    "No existe el archivo songs.json"
                )
            )

            return



        with open(
            file_path,
            encoding="utf-8"
        ) as file:

            songs = json.load(file)



        created = 0
        updated = 0
        albums_created = 0



        for song in songs:


            # Crear o encontrar álbum

            album, album_created = Album.objects.get_or_create(

                name=song["album"],

                defaults={

                    "album_type": "mini"

                }

            )


            if album_created:
                albums_created += 1



            # Crear o actualizar canción

            obj, was_created = Song.objects.update_or_create(

                title=song["title"],

                defaults={

                    "album": album,

                    "energy": song["energy"],

                    "vibe_tags": song["vibe_tags"],

                    "mood_keywords": song.get(
                        "mood_keywords",
                        ""
                    ),

                    "kimiko_review": song["kimiko_review"],

                    "youtube_url": song.get(
                        "youtube_url",
                        ""
                    ),

                    "spotify_url": song.get(
                        "spotify_url",
                        ""
                    ),

                }

            )



            if was_created:
                created += 1

            else:
                updated += 1




        self.stdout.write(

            self.style.SUCCESS(

                f"""
🐱 Discografía cargada correctamente

Álbumes nuevos: {albums_created}
Canciones nuevas: {created}
Canciones actualizadas: {updated}
"""

            )

        )