from django.contrib import admin

from .models import PortfolioModel, HomePageModel, AboutMeModel, ContactModel,PortfolioModelImages


    
class ProductImageAdmin(admin.StackedInline):
    model=PortfolioModelImages

@admin.register(PortfolioModel)
class PortfolioModel(admin.ModelAdmin):
    inlines=[ProductImageAdmin]
    
    
    
@admin.register(HomePageModel)
class HomePageModel(admin.ModelAdmin):
    pass

@admin.register(ContactModel)
class ContactModel(admin.ModelAdmin):
    pass

@admin.register(AboutMeModel)
class AboutMeModel(admin.ModelAdmin):
    pass