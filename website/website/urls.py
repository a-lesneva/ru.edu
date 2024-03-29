"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from website.apps.schools.sitemaps import SchoolsViewSitemap
from django.contrib.sitemaps.views import sitemap

# app_name='main'

sitemaps = {
    'schools_list': SchoolsViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('website.apps.main.urls')),
    # main page is school search for now 
    path('', include('website.apps.schools.urls')),
    path('users/', include('website.apps.users.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
]
