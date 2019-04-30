"""empresa URL Configuration

The `urlpatterns` list routes URLs to crud. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function crud
    1. Add an import:  from my_app import crud
    2. Add a URL to urlpatterns:  path('', crud.home, name='home')
Class-based crud
    1. Add an import:  from other_app.crud import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from empresa_web.views import home, show, create, update, delete, pageDelete,SignUp
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home', home, name='url_home'),
    path('funcionario/', show, name='url_show'),
    path('funcionario/create/', create, name='url_create'),
    path('funcionario/update/<int:pk>', update, name='url_update'),
    path('funcionario/delete/<int:pk>', delete, name='url_delete'),
    path('funcionario/pageDelete/<int:pk>',pageDelete, name='url_pageDelete'),
    path('cadastro', SignUp.as_view(), name='signup')

]