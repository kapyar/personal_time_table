"""rest_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from rest_service.views import hellow_world
from django.conf.urls import include
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [

	url('^schema/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hellow_world),
    url(r'^$', hellow_world),
    url(r'^raw_data/', include('raw_data.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
