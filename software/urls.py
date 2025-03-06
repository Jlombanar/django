
from django.contrib import admin
from django.urls import include, path
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
    path('separar/', views.separar, name='separar'),
    path('restablecer/', views.restablecer, name='restablecer'),
    path("cambiar_contraseña/<uidb64>/<token>/", views.cambiar_contraseña, name="cambiar_contraseña"),
    path("password_changed/", views.password_changed, name="password_changed"),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item, name='eliminar_item'),
    path('pasarela/', views.pasarela, name='pasarela'),
    path('confirmac/<int:orden_id>/', views.confirmacion, name='confirmar'),
   
]


if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)