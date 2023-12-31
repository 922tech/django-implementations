
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('home.urls'), name='home'),
    path('shop/', include('shop.urls'), name='shop'),
    path('blog/', include('weblog.urls'), name='blog'),
    path('ui/', include('ui.urls'), name='shop'),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path("__reload__/", include("django_browser_reload.urls")),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
