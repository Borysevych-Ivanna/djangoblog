from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Усі урли блогу
    path('', include('myblog.urls')),

    # Усі урли авторизації (login, logout, password_reset, …)
    path('accounts/', include('django.contrib.auth.urls')),
]
