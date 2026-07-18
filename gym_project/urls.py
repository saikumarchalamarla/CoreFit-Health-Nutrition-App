"""
URL configuration for gym_project project.

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
from gym_nutrition import views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gym-tips/', views.gym_tips, name='gym_tips'),
    path('nutrition-tips/', views.nutrition_tips, name='nutrition_tips'),
    path('contact/', views.contact_us, name='contact'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('add-to-cart/<int:sub_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path("health/", health),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)