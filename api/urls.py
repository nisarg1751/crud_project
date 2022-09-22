from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register('student' , views.CrudApi , basename='crudapi' )
# from sub import views

urlpatterns = [
    path('',include(router.urls)),
]
