from django.urls import path
from becados.views import BecasDetailView, PerfilView
#from comunidad.views import comunidad
from becados import views

urlpatterns = [
     path('becado/perfil', views.PerfilView.as_view()),
     path('becas', views.BecasDetailView.as_view())
]

