from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Contacts API",
      default_version='v1',
      description="API for contacts",
      terms_of_service="https://contacts/terms/",
      contact=openapi.Contact(email="contact@contact.local"),
      license=openapi.License(name="test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

  
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('authentication.urls')),
    path('api/contact/',include('contact.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
