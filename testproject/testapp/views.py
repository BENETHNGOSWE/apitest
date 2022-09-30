# from urllib import response
from calendar import prcal
from dataclasses import field
from inspect import Arguments
from pickle import FALSE
from shlex import quote
from django.shortcuts import render
from .models import Category, Mazao, Mkoa, Subcategory, Subcategoryinfo, Udongo, Wilaya, Udongomakundi, Udongotaarifa
from .serializers import MazaoSerializer, MkoaSerializer, WilayaSerializer, UdongoSerializer,UdongomakundiSerializer, UdongotaarifaSerializer, CategorySerializer,SubcategorySerializer,SubcategoryinfoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
import graphene

# Create your views here.
# **********************CATEGORIES DETAILS*****************************

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def list(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        data = serializer.data
        ct_id = data['id']
        subcategory = Subcategory.objects.filter(kundi=ct_id)
        serial = SubcategorySerializer(subcategory,many=True)
        context = {'subcategory': serial.data}
        data.update(context)
        return Response(data)
        
class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    
    
    def list(self,request, *args, **kwargs):
        queryset = Subcategory.objects.all()
        serializer = SubcategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Subcategory.objects.all()
        subcategory = get_object_or_404(queryset, pk=pk)
        serializer = SubcategorySerializer(subcategory)
        data = serializer.data
        sb_id = data['id']
        subcategoryinfo = Subcategoryinfo.objects.filter(kundijina=sb_id)
        serial = SubcategoryinfoSerializer(subcategoryinfo, many=True)
        context = {'subcategory': serial.data}
        data.update(context)
        return Response(data)
    
    
class SubcategoryinfoViewSet(viewsets.ModelViewSet):
    queryset = Subcategoryinfo.objects.all()
    serializer_class = SubcategoryinfoSerializer
    
    def list(self, request, pk=None):
        queryset = Subcategoryinfo.objects.all() 
        serializer = SubcategoryinfoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Subcategoryinfo.object.all()
        subcategoryinfo = get_object_or_404(queryset, pk=pk)
        serializer = SubcategoryinfoSerializer(subcategoryinfo)
        return Response(serializer.data)
        
        
           
           
                



# **********************************************************************
class MkoaViewSet(viewsets.ModelViewSet):
    queryset = Mkoa.objects.all()
    serializer_class = MkoaSerializer
    
    def list(self, request):
        queryset = Mkoa.objects.all()
        serializer = MkoaSerializer(queryset, many=True)
        return Response(serializer.data)

# class createMkoa(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
#     success = graphene.Boolean()
    
#     def mutate(self,name, info):
#         mkoa_object, created = Mkoa.objects.get_or_create(name=name)
#     return createMkoa(success=created)
        
    
    
  
    # return Response(serializer)
    
    # def data (self, request) :
    #     queryset = Mkoa.objects.filter(name=self.request.user)
    #     serializer = MkoaSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    
    
    
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def getWilaya(request):
    print(request.data)
    mkoa_id = request.data['id']      
    
    
    
    
    
    
    
    
    
        # queryset = Mkoa.objects.all()
        # return queryset
    
    # def retrieve(self, request, pk=None):
    #     queryset = Mkoa.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = MkoaSerializer(user)
    #     return Response(serializer.data)
        
    # def retrieve(slef, request, **kwargs):fields : '__all__'   
    #      serializer = MkoaSerializer(mkoajina, many=False)
    #      data = serializer.data
    #      mk_id = data['id']
    #      wilaya = Wilaya.objects.filter(jinalamkoa=mk_id)
    #      serial = WilayaSerializer(wilaya, many=True)
    #      x = {'wilaya': serial.data}
    #      data.update(x)
    #      return Response(data)   
    

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        
#  print(params['pk'])
    mkoajina = Mkoa.objects.get(id=mkoa_id)
    serializer = MkoaSerializer(mkoajina, many=False)
    data = serializer.data
#  mk_id = data['id']
    wilaya = Wilaya.objects.filter(jinalamkoa=mkoa_id)
    serial = WilayaSerializer(wilaya, many=True)
    x = {'wilaya': serial.data}
    data.update(x)
    return Response(data)

 
class WilayaViewSet(viewsets.ModelViewSet):
    queryset = Wilaya.objects.all()
    serializer_class = WilayaSerializer
    
    def list(self, request):
        queryset = Wilaya.objects.all()
        serializer = WilayaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def getwilayainfo(request):
    print(request.data)
    wl_id = request.data['id']
    wilayajina = Wilaya.objects.get(id=wl_id)
    serializer = WilayaSerializer(wilayajina, many=False)
    data = serializer.data
    wl_id=data['id']
    mazao=Mazao.objects.filter(jinalawilaya=wl_id)
    udongo=Udongo.objects.filter(jinalawilaya=wl_id)
    serial = MazaoSerializer(mazao, many=True)
    serial2 = UdongoSerializer(udongo, many=True)
    context = {'mazao': serial.data}
    context2 = {'udongo': serial2.data}
    data.update(context)
    data.update(context2)
    return Response(data)    


    
    # def get(self, request, format=None):
    #     wilaya = Wilaya.objects.all()
    #     serializer = WilayaSerializer(wilaya, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = WilayaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # def get(self, request,  *args, **kwargs):
    #      params = kwargs
    #      if request.method == 'GET':
    #         wilaya = Wilaya.objects.all()
    #         serializer = WilayaSerializer(wilaya, many=True)
    #         return Response(serializer.data)
    
    #      else:
    #          wilayajina = Wilaya.objects.filter(jinalawi http://172.17.17.75:8000/laya = params['pk'])
    #          serializer = WilayaSerializer(wilayajina, many=True)
    #          return Response(serializer.data) 
    # def data(self, request):
    #     queryset = Wilaya.objects.all()
    #     return queryset
    
    # def retrieve(self, request, name=None, **kwargs):fields : '__all__'   
    #         wilayas = Wilaya.objects.all()
    #         mkoa = Mkoa.objects.filter(wilaya=wilaya,many=True)
            
    #         context = {
    #             'wilayas': wilayas,
    #             'wilaya':wilaya,
    #             'mkoa': mkoa
    #         }
    #         return render(request,context)
    #     else:
    #         wilayas=Wilaya.objects.all()
    #         http://172.17.17.75:8000/
    # def retrieve(slef, request, *args, **kwargs):
    #      params = kwargs
    #     #  print(params['pk'])return get_object_or_404(Container, id=self.kwargs['pk']) ina, many=False)
    #      data = serializer.data
    #      wl_id=data['id']
    #      mazao=Mazao.objects.filter(jinalawilaya=wl_id)
    #      udongo=Udongo.objects.filter(jinalawilaya=wl_id)
    #      serial = MazaoSerializer(mazao, many=True)
    #      serial2 = UdongoSerializer(udongo, many=True)
    #     #  serial = MazaoSerializer, UdongoSerializer(mazao,udongo, many=True)
    #     #  context = [{'mazao': serial.data}, {'udongo': serial.data}]
    #      context = {'mazao': serial.data}
    #      context2 = {'udongo': serial2.data}
    #     #  context = {'udongo': serial.data}
    #      data.update(context)
    #      data.update(context2)
    #      return Response(data)
    #     #  return Response(serializer.data)
# *****************************************************************************************
        
     

         
# ***************************************************************************************
   
class MazaoViewSet(viewsets.ModelViewSet):
    queryset = Mazao.objects.all()
    serializer_class = MazaoSerializer
    
    def list(self, request):
        queryset = Mazao.objects.all()
        serializer = MazaoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def retrieve(slef, request, *args, **kwargs):
         params = kwargs
         print(params['pk'])
         jinalamazao = Mazao.objects.filter(jinalamazao = params['pk'])
         serializer = MazaoSerializer(jinalamazao, many=True)
         return Response(serializer.data)


# *****************************************************************************************************
class UdongoViewSet(viewsets.ModelViewSet):
    queryset = Udongo.objects.all()
    serializer_class = UdongoSerializer
    
    def list(self, request):
        queryset = Udongo.objects.all()
        serializer = UdongoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        jinalaudongo=Udongo.objects.filter(jinalaudongo, params['pk'])
        serializer = UdongoSerializer(jinalaudongo, many=True)
        return Response(serializer.data)
       
class UdongotaarifaViewSet(viewsets.ModelViewSet):
    queryset = Udongotaarifa.objects.all()
    serializer_class = UdongotaarifaSerializer
    
    def list(self,request, *args, **kwargs):
        queryset = Udongotaarifa.objects.all()
        serializer = UdongotaarifaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Udongotaarifa.objects.all()
        udongotaarifa = get_object_or_404(queryset, pk=pk)
        serializer = UdongotaarifaSerializer(udongotaarifa)
        return Response(serializer.data)
    
class UdongomakundiViewSet(viewsets.ModelViewSet):
    queryset = Udongomakundi.objects.all()
    serializer_class=UdongomakundiSerializer
    
    def list(self,request, *args, **kwargs):
        queryset = Udongomakundi.objects.all()
        serializer = UdongomakundiSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        queryset = Udongomakundi.objects.all()
        udongomakundi = get_object_or_404(queryset, pk=pk)  
        serializer = UdongomakundiSerializer(udongomakundi)
        data = serializer.data
        ud_id=data['id']
        udongotaarifa = Udongotaarifa.objects.filter(ainayaudongo=ud_id)
        serial = UdongotaarifaSerializer(udongotaarifa, many=True)
        context = {'udongotaarifa': serial.data}
        data.update(context)
        return Response(data)    
  
    
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def getudongoinfo(request):
#     udongo_id = request.data['id']  
#     udongojina = Udongo.objects.get(id=udongo_id)
#     serializer = UdongoSerializer(udongojina=udongo_id)
#     return Response(serializer) 
        

# POINT OF VIEWS**********):
#     if request.method == "GET":
#         return Response({'message':'hey get'})
#     if request.method == "POST":
#         print(request)
#         return Response({'message': 'hey post'})