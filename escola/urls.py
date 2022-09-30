from django.contrib import admin
from django.urls import path
from cadastro.views import cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro)
]
