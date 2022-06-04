
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from dapi import views 


from rest_framework.routers import DefaultRouter

router =DefaultRouter()
router.register('home',views.HomePageViewSet)
router.register('about',views.AboutViewSet)
router.register('portfolio',views.PortfolioViewSet)
router.register('contact',views.ContactViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
