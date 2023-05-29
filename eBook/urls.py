from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # swagger
    path("server/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "server/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("admin/", admin.site.urls),
    path("server/", include("book.urls"), name="books_base_API"),
    path("server/", include("celebrity.urls"), name="celebrity_base_API"),
    path("server/", include("user.urls"), name="users_base_API"),
    path("server/auth/login/", TokenObtainPairView.as_view(), name="token_create"),
    path("server/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)