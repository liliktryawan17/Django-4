from django.urls import path
from . import views

urlpatterns = [
    path('', views.konten),
    path('new/', views.new),
    path('popular/', views.popular)
]
