from django.urls import path
from . import views
urlpatterns = [
    path('Clients/', views.Clients, name='Clients'),
]