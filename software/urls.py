
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from web import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('productos/', views.productos, name='productos'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('contactenos/', views.contactenos, name='contactenos'),
    

] 

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)