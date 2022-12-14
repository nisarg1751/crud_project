"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from sub import views
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add,name='home'),
    path('add/', views.adddata,name='add'),
    # path('update/', views.update),
    path('delete/<int:id>/',views.delete_data, name='deletedata'),
    path('<int:id>/',views.update, name='updatedata'),
    path('sucessful',views.thankyou,name='successful'),
    path('api/',include('api.urls'))


]
