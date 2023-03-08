from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', admin.site.urls),
    path('api/v1/', include('recipes.urls', namespace='recipes')),
]
