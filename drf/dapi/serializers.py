from rest_framework import serializers

from .models import PortfolioModel,AboutMeModel,HomePageModel,ContactModel,PortfolioModelImages

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model=HomePageModel
        fields=('text1','text2','text3','paragraph','image')
        
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutMeModel
        fields=('image','paragraph','experience','e_year','skill_sub','s_percents')
        
        
        
        
class PortfolioModelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PortfolioModelImages
        fields=('image','project',"created_at")
        
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=PortfolioModel
        fields=('title','slug','description','thumbnail','date_created')
        slug_field='slug'
        url_field='get_absolute_url'
        
        
        

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactModel
        fields=('firstname','lastname','email','phone','messages','date_created')
    