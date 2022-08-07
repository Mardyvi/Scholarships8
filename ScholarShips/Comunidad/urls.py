from django.urls import path
from Comunidad import views

urlpatterns = [
    path('', views.ComunidadView.as_view()),
    path('listar/', views.ListComunidad.as_view()) 
]