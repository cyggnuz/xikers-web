from django.db import models
from datetime import date


class Member(models.Model):
    # Nombre artístico, el que se muestra en la tarjeta principal
    stage_name = models.CharField(max_length=50)

    # Nombre real completo, opcional
    real_name = models.CharField(max_length=100, blank=True)

    # Fecha de nacimiento: NO guardamos la edad como número fijo,
    # porque quedaría desactualizada. La calculamos siempre a partir
    # de esta fecha (ver el metodo age mas abajo).
    birth_date = models.DateField()

    # Posicion dentro del grupo, ej: "Leader, Vocalist"
    position = models.CharField(max_length=100, blank=True)

    # Foto principal subida y almacenada en el servidor (se guarda en media/members/)
    # Este es el RENDER grande que aparece a la derecha.
    photo = models.ImageField(upload_to='members/', blank=True)

    # 🖼️ Foto cuadrada para la ficha técnica (columna izquierda)
    # Esta es la que marcaste en la imagen. Se guarda en media/members/thumbnails/
    thumbnail_photo = models.ImageField(
        upload_to='members/thumbnails/', 
        blank=True, 
        null=True,
        help_text="Foto cuadrada pequeña para la ficha de la izquierda."
    )

    # 🖼️ Foto/Marco secundario para la zona blanca izquierda de la tarjeta (gráfica de fondo)
    secondary_photo = models.ImageField(
        upload_to='members/secondary/', 
        blank=True, 
        null=True,
        help_text="Imagen o detalle para el espacio recuadrado a la izquierda (gráfica de fondo)"
    )

    # Texto corto para la ficha
    bio = models.TextField(blank=True)

    # Orden en que aparece en la lista/sidebar (0 = primero)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.stage_name

    @property
    def age(self):
        """
        Calcula la edad actual a partir de birth_date, comparando
        con la fecha de hoy. Se recalcula cada vez que se llama,
        asi que siempre esta actualizada sin necesidad de tareas
        programadas ni de editar el dato a mano.
        """
        today = date.today()
        years = today.year - self.birth_date.year
        # Resta 1 si todavia no ha llegado el cumpleaños este año
        birthday_passed = (today.month, today.day) >= (self.birth_date.month, self.birth_date.day)
        if not birthday_passed:
            years -= 1
        return years

    @property
    def is_birthday_today(self):
        """
        True si hoy es el cumpleaños del integrante.
        Se usa en el template para mostrar el banner de felicitacion.
        """
        today = date.today()
        return (today.month, today.day) == (self.birth_date.month, self.birth_date.day)
    
    COLOR_CHOICES = [
        ('#E63946', 'Rojo'),
        ('#FFD21F', 'Amarillo'),
        ('#147DFF', 'Azul'),
        ('#2ECC71', 'Verde'),
        ('#9B59B6', 'Morado'),
        ('#F5F5F5', 'Blanco'),
    ]

    favorite_color = models.CharField(
        max_length=7,
        choices=COLOR_CHOICES,
        default='#FFD21F',
    )