# from urllib import response
from calendar import prcal
from dataclasses import field
from django.shortcuts import render
from .models import Mazao, Mkoa, Wilaya
from .serializers import MazaoSerializer, MkoaSerializer, WilayaSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

class MkoaViewSet(viewsets.ModelViewSet):
    queryset = Mkoa.objects.all()
    serializer_class = MkoaSerializer
    
    
    # return Response(serializer)
    
    # def data (self, request) :
    #     queryset = Mkoa.objects.filter(name=self.request.user)
    #     serializer = MkoaSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    def list(self, request):
        queryset = Mkoa.objects.all()
        serializer = MkoaSerializer(queryset, many=True)
        return Response(serializer.data)
        # queryset = Mkoa.objects.all()
        # return queryset
    
    # def retrieve(self, request, pk=None):
    #     queryset = Mkoa.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = MkoaSerializer(user)
    #     return Response(serializer.data)
        
    def retrieve(slef, request, *args, **kwargs):
         params = kwargs
        
        #  print(params['pk'])
         mkoajina = Mkoa.objects.get(name = params['pk'])
         serializer = MkoaSerializer(mkoajina, many=False)
         data = serializer.data
         mk_id = data['id']
         wilaya = Wilaya.objects.filter(jinalamkoa=mk_id)
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
    
    
    # def get(self, request,  *args, **kwargs):
    #      params = kwargs
    #      if request.method == 'GET':
    #         wilaya = Wilaya.objects.all()
    #         serializer = WilayaSerializer(wilaya, many=True)
    #         return Response(serializer.data)
    
    #      else:
    #          wilayajina = Wilaya.objects.filter(jinalawilaya = params['pk'])
    #          serializer = WilayaSerializer(wilayajina, many=True)
    #          return Response(serializer.data) 
    # def data(self, request):
    #     queryset = Wilaya.objects.all()
    #     return queryset
    
    # def retrieve(self, request, name=None, **kwargs):
    #     if wilaya:
    #         wilaya = Wilaya.objects.get(slug=wilaya)
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
    #         mkoa = Mkoa.objects.filter(many=True)
    #         return render(request, context)
            
        
        
    def retrieve(slef, request, *args, **kwargs):
         params = kwargs
        #  print(params['pk'])
         wilayajina = Wilaya.objects.filter(jinalawilaya = params['pk'])
         serializer = WilayaSerializer(wilayajina, many=True)
         return Response(serializer.data)
     
     
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


# POINT OF VIEWS**********
# @api_view(['GET','POST'])
# @permission_classes([AllowAny])

# def Demo(request):
#     if request.method == "GET":
#         return Response({'message':'hey get'})
#     if request.method == "POST":
#         print(request)
#         return Response({'message': 'hey post'})