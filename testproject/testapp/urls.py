from lib2to3.pgen2.token import RPAR
from .models import Mkoa, Wilaya
from .views import MkoaViewSet, WilayaViewSet, MazaoViewSet
from rest_framework import routers 
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'demo', MkoaViewSet)
router.register(r'demo2', WilayaViewSet)
router.register(r'demo3', MazaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('/hey',Demo),
]



