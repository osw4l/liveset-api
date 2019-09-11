from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import base as settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


schema_view = get_swagger_view(title='Django osw4l boilerplate API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('', schema_view),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

