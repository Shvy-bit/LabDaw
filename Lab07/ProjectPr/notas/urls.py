from django.urls import path
from . import views
urlpatterns = [
    path('guardar/', views.guardar_nota, name='guardar_nota'),
    path('', views.lista_notas, name='lista_notas'),
]