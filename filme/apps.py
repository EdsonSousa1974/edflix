from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

def ready(self):
    #from .models import Usuario
    from django.contrib.auth.models import Usuario; 
    import os
    
    email_os = os.getenv("EMAIL_ADMIN")
    senha_os = os.getenv("SENHA_ADMIN")
    
    #if not Usuario.objects.filter(email=email_os).exists():
    usuarios = Usuario.objects.filter(email=email_os)    
    
    #if not usuarios:
    usuarios.objects.create_superuser(username="admin", email=email_os, password=senha_os)
#                                         is_active=True, is_staff=True)
