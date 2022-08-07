import imp
from django.urls import path
from organizacion import views

urlpatterns = [
    path('', views.OrgView.as_view(), name='index'),
]
