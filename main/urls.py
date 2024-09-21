from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from gym_mang_syst.settings import MEDIA_ROOT


from . import views
urlpatterns = [
    path('',views.home, name='home'),
    

    
    
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)