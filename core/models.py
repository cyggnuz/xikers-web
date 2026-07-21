from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    role = models.CharField(max_length=100, verbose_name="Rol / Posición")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden de visualización")
    image = models.ImageField(upload_to='members/', verbose_name="Foto Teaser")
    is_active = models.BooleanField(default=True, verbose_name="¿Mostrar en el Roster?")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Integrante"
        verbose_name_plural = "Integrantes"

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    role = models.CharField(max_length=100, verbose_name="Rol / Posición")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden de visualización")
    image = models.ImageField(upload_to='members/', verbose_name="Foto Teaser (Frente)")
    # 🎯 Nuevo campo para la foto del reverso
    back_image = models.ImageField(upload_to='members/back/', blank=True, null=True, verbose_name="Foto Reverso (Back)")
    is_active = models.BooleanField(default=True, verbose_name="¿Mostrar en el Roster?")