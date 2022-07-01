from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('myblog/', include('myblog.urls')),
    path('mycontent/', include('mycontent.urls'))
]
