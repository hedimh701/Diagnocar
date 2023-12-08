"""
URL configuration for diagnocarFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls')),
    path('code/', include('errorCode.urls')),
    path('post/', include('post.urls')),
    path('administration/', include('subscription.urls')),

]

admin.site.site_header=  "Diagnocar Administration"  
admin.site.site_title  =  "Diagnocar"
admin.site.index_title  =  "Diagnocar"