from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('check_user/', views.check_user, name='check_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)