# url - view - templante

from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilmes, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_views

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisafilmes/', Pesquisafilmes.as_view(), name='pesquisafilmes'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),    
    path('editarperfil/', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
]
