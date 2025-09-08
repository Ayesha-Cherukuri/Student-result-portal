from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portalapp.urls')),   # your app urls
    path('', include('django.contrib.auth.urls')),  # 🔑 add this line
]
