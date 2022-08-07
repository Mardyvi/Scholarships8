import imp
from django.urls import path
from organizacion import views
from .views import OrgUpdateDeleteView, OrgView

urlpatterns = [
    path('', views.OrgView.as_view()),
    path('<int:id>/', views.OrgUpdateDeleteView.as_view()),
]
