from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('register.urls')),
    path('', include('higherlower.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'))
]
