from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from student.permissions import IsAdminUserorAuthenticated

schema_view = get_schema_view(
    openapi.Info(
        title="gg-core api",
        default_version="v1",
        #   description="Test description",
        #   terms_of_service="https://www.google.com/policies/terms/",
        #   contact=openapi.Contact(email="contact@snippets.local"),
        #   license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(IsAdminUserorAuthenticated,),
)

urlpatterns = [
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/", include("student.urls")),
    path("auth/", include("djoser.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
