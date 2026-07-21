import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xikers_site.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Modifica con tus datos para ingresar al admin
USERNAME = 'cyggnuz'
EMAIL = 'apeg1999@gmail.com'
PASSWORD = 'Churrascowaton1'  # 👈 Cambia esto por la clave que quieras usar

if not User.objects.filter(username=USERNAME).exists():
    print(f"Creando superusuario {USERNAME}...")
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print("¡Superusuario creado con éxito!")
else:
    print(f"El superusuario {USERNAME} ya existe.")