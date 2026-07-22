import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xikers_site.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME")
EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL")
PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print("Superusuario creado.")
else:
    print("El superusuario ya existe.")