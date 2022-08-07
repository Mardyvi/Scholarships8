from django.urls import path
from .views import BecaView

urlpatterns = [
    path('', BecaView.as_view()),
]