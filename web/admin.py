from django.contrib import admin
from web.models import Libro
from .models import Producto

# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    model = Libro
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_display_links = ('titulo',)

admin.site.register(Libro, LibroAdmin)




class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('nombre', 'precio', 'fecha_creacion','foto')
    list_display_links = ('nombre',)

admin.site.register(Producto, ProductoAdmin)
