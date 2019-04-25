"""empresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from empresa_web.views import home, show, create, update, delete, pageDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('funcionario/', show, name='url_show'),
    path('funcionario/create/', create, name='url_create'),
    path('funcionario/update/<int:pk>', update, name='url_update'),
    path('funcionario/delete/<int:pk>', delete, name='url_delete'),
    path('funcionario/pageDelete/<int:pk>',pageDelete, name='url_pageDelete')
]