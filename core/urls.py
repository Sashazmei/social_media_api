from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def index(request):
    return JsonResponse({"message": "Добро пожаловать в Social Media API!"}, json_dumps_params={'ensure_ascii': False})

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/posts/', include('posts.urls')),

]
schema_view = get_schema_view(
   openapi.Info(
      title="Social Media API",
      default_version='v1',
      description="Документация для Social Media API",
      contact=openapi.Contact(email="your@email.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
