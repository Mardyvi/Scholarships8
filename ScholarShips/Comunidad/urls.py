from django.urls import path
from Comunidad import views
from Comunidad.views import UpdateComunidad, DeleteComunidad

urlpatterns = [
    path('', views.ComunidadView.as_view()),
    path('listar/', views.ListComunidad.as_view()),
    #path('updateComunidad/<int:pk>/', views.UpdateComunidad.as_view(),),
    path('deleteComunidad/<int:pk>/', views.DeleteComunidad.as_view(),),
]