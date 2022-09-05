"""homebanking URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from prueba import views as pruebas_views
from portafolio import views as portafolio_views
from contact import views as contact_views
from prestamo import views as prestamo_views
from tarjeta import views as tarjeta_views


urlpatterns = [
    path('', pruebas_views.home, name="home"),
    path('about/', pruebas_views.about, name="about"),
    path('portafolio/', portafolio_views.portafolio, name="portafolio"),
    path('contact/', contact_views.contact, name="contact"),
    path('prestamo/', prestamo_views.prestamo, name="prestamo"),
    path('tarjeta/', tarjeta_views.tarjetas, name="tarjeta"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)