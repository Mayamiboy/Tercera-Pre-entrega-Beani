"""
URL configuration for mysiteweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysiteweb.urls')),
]


from django.urls import path
from . import view  # Asegúrate de importar el archivo view.py correctamente

urlpatterns = [
    path('', view.home, name='home'),
    path('add_author/', view.add_author, name='add_author'),
    path('search_author/', view.search_author, name='search_author'),
    path('saludo/', view.saludo, name='saludo'),
    path('dia_de_hoy/', view.dia_de_hoy, name='dia_de_hoy'),
    path('mi_nombre/<str:nombre>/', view.mi_nombre, name='mi_nombre'),
]
