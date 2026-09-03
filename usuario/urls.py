from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),

    path(
        'cadastro/',
        views.cadastro,
        name='cadastro'
    ),

    path(
        'disciplinas/',
        views.filtrar_disciplinas,
        name='filtrar_disciplinas'
    ),

    path(
        'home/',
        views.home,
        name='home'
    ),
]