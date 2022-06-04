from django.db import models
from django.core.validators import EmailValidator
from django.core.validators import MinLengthValidator

from django.core.exceptions import ValidationError



from io import BytesIO
from django.core.files import File
# from PIL import Image
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars


from django.urls import reverse


from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


from django.core.validators import RegexValidator

class HomePageModel(models.Model):
    text1=models.CharField(max_length=200)
    text2=models.CharField(max_length=200)
    text3=models.CharField(max_length=200)
    paragraph=models.CharField(max_length=450)
    image=models.ImageField(upload_to='home/images/', blank=True, null=True)
    
    def __str__(self):
        return self.text1
    
    
class AboutMeModel(models.Model):
    
    image=models.ImageField(upload_to='about/images/'  )
    paragraph=models.TextField()
    experience=models.TextField()
    e_year=models.DateTimeField(auto_now_add=False)
    skill_sub=models.CharField(max_length=200)
    s_percents=models.IntegerField()

    def __str__(self):
        return self.paragraph
 
 
class PortfolioModel(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True,blank=True,null=True)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to='portfolio/images/' )
    # images=models.ImageField(upload_to='portfolio/images/'  )
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'slug':self.slug})
    # image resize function
    
    def truncate(self):
        return truncatechars(self.description, 100)
    
class PortfolioModelImages(models.Model):
    project=models.ForeignKey("PortfolioModel", related_name="project" ,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='portfolio/images/', blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project.title
    
    
@receiver(pre_save, sender=PortfolioModel)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        

class ContactModel(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,validators=[EmailValidator])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    messages=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return self.firstname+" "+ self.lastname+" "+ self.email
    
    

