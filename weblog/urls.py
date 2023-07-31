from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'post',PostCRUD)
router.register(r'category',CategoryCrud)

urlpatterns = [
    path('mypost/<str:slug>', get_post),
    path('user/', log_user),
    

] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

