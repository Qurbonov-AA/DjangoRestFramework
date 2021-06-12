from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-base', include('rest_framework.urls')),
    path('rest/v1/', include('mytestapp.urls'), name="API"),
    
]
