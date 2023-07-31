
from django.urls import path
from django.conf.urls.static import static
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products',ProductCRUD)
# print(f'***\n\n{router.urls}***\n\n')
urlpatterns = [

] + router.urls



