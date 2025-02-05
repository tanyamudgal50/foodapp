"""
URL configuration for foodapp project.

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
from django.urls import path
from foodaskerapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('restaurant/sign-in/', auth_views.LoginView.as_view(
        template_name='restaurant/sign_in.html'), name='restaurant-sign-in'),
    path('restaurant/sign-out', auth_views.LogoutView.as_view(next_page='/'),
         name = 'restaurant-sign-out'),
    path('restaurant/sign-up/', views.restaurant_sign_up, name='restaurant-sign-up'),
    path("restaurant/", views.restaurant_home, name="restaurant_home"),
    path('restaurant/Menu-Item/', views.restaurant_add_menu_item, name='restaurant-Menu-Item'),
    path('restaurant/Order-Details/', views.restaurant_Order_Details, name='restaurant-Order-Details'),
    path('restaurant/delivery/', views.restaurant_delivery, name='restaurant-delivery'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

