"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('crear-caso/', views.CrearCaso, name='crear_caso'),
    path('crear-tipo-caso/', views.CrearTipoCaso, name='crear_tipo_caso'),
    path('crear-tipo-dispositivo/', views.CrearTipoDispositivo, name='crear_tipo_dispositivo'),
    path('crear-marca/', views.CrearMarca, name='crear_marca'),
    path('crear-modelo/', views.CrearModelo, name='crear_modelo'),
    path('caso-detalle/<id>', views.CasoDetalle, name='caso_detalle'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('guardar/<estado>/<fecha>/<monto>/<id>', views.Guardar, name='guardar'),
    path('eliminar/<id>', views.Eliminar, name='eliminar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
