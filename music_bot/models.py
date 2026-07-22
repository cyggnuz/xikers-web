from django.db import models


class Album(models.Model):

    ALBUM_TYPES = [
        ("mini", "Mini Album"),
        ("single", "Single"),
        ("japanese", "Japanese Release"),
        ("special", "Special"),
    ]


    name = models.CharField(
        max_length=150,
        verbose_name="Nombre del álbum"
    )


    release_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de lanzamiento"
    )


    album_type = models.CharField(
        max_length=20,
        choices=ALBUM_TYPES,
        default="mini",
        verbose_name="Tipo de lanzamiento"
    )


    cover = models.ImageField(
        upload_to="albums/",
        blank=True,
        null=True,
        verbose_name="Portada del álbum"
    )


    description = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbumes"
        ordering = ["-release_date", "name"]


    def __str__(self):
        return self.name





class Song(models.Model):

    ENERGY_CHOICES = [
        ('high', '⚡ Alta / Potente'),
        ('medium', '🎧 Media / Balanceada'),
        ('low', '🌙 Tranquila / Chill'),
    ]


    title = models.CharField(
        max_length=100,
        verbose_name="Título de la Canción"
    )


    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="songs",
        verbose_name="Álbum"
    )


    energy = models.CharField(
        max_length=10,
        choices=ENERGY_CHOICES,
        verbose_name="Nivel de Energía"
    )


    # Etiquetas visuales de la canción
    # Ej: oscuro, épico, divertido, rebelde
    vibe_tags = models.TextField(
        help_text="Ej: oscuro, epico, divertido, emocional",
        verbose_name="Vibra / Tags"
    )


    # Palabras que Kimiko puede detectar
    # Ej: feliz, triste, estudiar, bailar, noche
    mood_keywords = models.TextField(
        blank=True,
        help_text="Ej: feliz, bailar, motivación, noche, energía",
        verbose_name="Palabras clave de Kimiko"
    )


    # Mensaje personalizado de Kimiko
    kimiko_review = models.TextField(
        help_text="Mensaje que dirá Kimiko al recomendar esta canción.",
        verbose_name="Recomendación de Kimiko"
    )


    youtube_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link de YouTube / MV"
    )


    spotify_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link de Spotify"
    )


    cover_image = models.ImageField(
        upload_to='songs/',
        blank=True,
        null=True,
        verbose_name="Portada individual"
    )


    song_type = models.CharField(
        max_length=50,
        blank=True,
        help_text="Ej: title track, b-side, intro, special",
        verbose_name="Tipo de canción"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"
        ordering = ['album__name', 'title']


    def __str__(self):
        return f"{self.title} - {self.album.name}"