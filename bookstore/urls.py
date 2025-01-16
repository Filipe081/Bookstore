"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
=======
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
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
import debug_toolbar
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, re_path, include
=======
from django.urls import include, path, re_path
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
=======
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
>>>>>>> dc470303bf4b28221614af9800d5dea6727be939
