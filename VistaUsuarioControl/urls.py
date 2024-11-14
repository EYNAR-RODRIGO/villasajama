from django.urls import path
from .import views
# importar login

urlpatterns = [
    path('',views.Menu_Principal,name='MenuPrincipal'),
    path('camaraqr',views.Camara,name='camara'),
]
