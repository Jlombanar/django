from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered  # Importación necesaria
from .models import CarritoItem, Datos, Orden, OrdenItem, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'fecha_creacion', 'foto')
    list_display_links = ('nombre',)

admin.site.register(Producto, ProductoAdmin)

class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'usuario', 'sesion_id', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('producto__nombre', 'usuario__username')

try:
    admin.site.register(CarritoItem, CarritoItemAdmin)
except AlreadyRegistered:
    pass

class AdminPerfilUsuario(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellido')    

admin.site.register(Datos, AdminPerfilUsuario)

class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    extra = 0
    readonly_fields = ('producto', 'precio', 'cantidad')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono', 'total', 'pagado', 'fecha_creacion')
    list_filter = ('pagado', 'fecha_creacion','metodo_pago')
    search_fields = ('nombre', 'email')
    inlines = [OrdenItemInline]  # Agregamos los productos dentro de la orden

try:
    admin.site.register(Orden, OrdenAdmin)
except AlreadyRegistered:
    pass
