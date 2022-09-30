# from dataclasses import fields
from dataclasses import fields
from pyexpat import model
from .models import Mkoa, Wilaya, Mazao, Udongo, Udongomakundi, Udongotaarifa, Category,Subcategory,Subcategoryinfo
from rest_framework import serializers
# *********************CATEGORIES DETAILS*****************************

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
        
class SubcategoryinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoryinfo
        fields = '__all__'                

# ********************************************************************
class MkoaSerializer(serializers.ModelSerializer):
    mkoa_id = serializers.IntegerField(read_only=True, source='id')
    class Meta:
        model = Mkoa
        fields = '__all__'
        
class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = '__all__'     
        
class MazaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mazao
        fields = '__all__'   
#***************************************************************************************** 
class UdongoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Udongo
        fields = '__all__'                                     
        
class UdongotaarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Udongotaarifa
        fields = '__all__'    
        
class UdongomakundiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Udongomakundi
        fields = '__all__'        