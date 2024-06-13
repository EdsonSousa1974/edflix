from django.apps import AppConfig

from environs import Env
env = Env()
env.read_env()

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
"""
    def ready(self):
        from .models import Usuario
        import os
        
        email_os = os.environ.get("EMAIL_ADMIN")        
        senha_os = os.environ.get("SENHA_ADMIN")
        
        usuarios = Usuario.objects.filter(username="admin")    
        if not usuarios:
            Usuario.objects.create_superuser(username="admin", email=email_os, password=senha_os,
                                             is_active=True, is_staff=True)
#"""                                             
