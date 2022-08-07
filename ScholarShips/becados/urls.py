from django.urls import path
from becados.views import PerfilAPIView
#from comunidad.views import comunidad
from becados import views

urlpatterns = [
     path('perfil/', views.PerfilAPIView.as_view()),
     #path('becas', views.BecasDetailView.as_view())
]

