from django.urls import path
from becados.views import BecadoBecadosListView

urlpatterns = [
     path('becados/<becado>/',
BecadoBecadosListView.as_view()),
]

