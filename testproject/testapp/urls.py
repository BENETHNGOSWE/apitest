from lib2to3.pgen2.token import RPAR
from .models import Mkoa, Wilaya
from .views import MkoaViewSet, WilayaViewSet, MazaoViewSet, UdongoViewSet,UdongomakundiViewSet,UdongotaarifaViewSet, getWilaya, getwilayainfo, CategoryViewSet,SubcategoryinfoViewSet,SubcategoryViewSet
from rest_framework import routers 
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'demo', MkoaViewSet)
router.register(r'demo2', WilayaViewSet)
router.register(r'demo3', MazaoViewSet)
router.register(r'demo4', UdongoViewSet)
router.register(r'demo7', UdongotaarifaViewSet)
router.register(r'demo8', UdongomakundiViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubcategoryViewSet)
router.register(r'subcategoryinfo', SubcategoryinfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('/demo5',getWilaya),
    path('/demo6', getwilayainfo),
    # path('/demo7', getudongoinfo)
]



