from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()



class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='web/static/img')
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
