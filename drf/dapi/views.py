from django.shortcuts import render

from .serializers import HomePageSerializer,AboutSerializer,PortfolioSerializer,ContactSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HomePageModel,AboutMeModel,PortfolioModel,ContactModel


class HomePageViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = HomePageModel.objects.all()
    serializer_class = HomePageSerializer
    

class AboutViewSet (viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = AboutMeModel.objects.all()
    serializer_class = AboutSerializer
    
class PortfolioViewSet (viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PortfolioModel.objects.all()
    serializer_class = PortfolioSerializer
    
class ContactViewSet (viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    
    
    
    
    
