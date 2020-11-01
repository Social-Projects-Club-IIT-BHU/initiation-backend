from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index', views.index, name="index"),
]


# for static files

urlpatterns += static('img/', document_root= settings.BASE_DIR / 'homepage/static/img')
urlpatterns += static('js/', document_root= settings.BASE_DIR / 'homepage/static/js')
urlpatterns += static('css/', document_root= settings.BASE_DIR / 'homepage/static/css')
urlpatterns += static('fonts/', document_root= settings.BASE_DIR / 'homepage/static/fonts')
