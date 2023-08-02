
from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products',ProductCRUD)

urlpatterns = [
] + router.urls



