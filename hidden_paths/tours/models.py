from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Tours(models.Model):
    nombre_tour = models.CharField(max_length=100,verbose_name="Nombre del tour")
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=100,verbose_name="Nombre del estado")
    ciudad = models.CharField(max_length=100,verbose_name="Nombre de la ciudad")
    km_recorrido = models.CharField(max_length=100,verbose_name="Distancia")
    tiempo_estimado = models.CharField(max_length=100,verbose_name="Tiempo estimado")
    punto_inicio = models.CharField(max_length=100,verbose_name="Punto de partida")
    costo = models.FloatField(verbose_name="Costo del tour")
    ganancias = models.FloatField(verbose_name="Ganancia")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(null=True,upload_to="fotos", verbose_name="Foto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de inserción")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")
   
    

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"
        ordering = ["created"]
    
    def __str__(self):
        return self.nombre_tour
    
    

class Review(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User
    rating = models.IntegerField(max_length=5, validators=[
            MaxValueValidator(5),  # Valor máximo de 5
            MinValueValidator(1)   # Valor mínimo de 1 (opcional)
        ])
    comment = models.TextField()
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)


    def __str__(self):
        return f"Review by {self.user.username} for {self.tour.nombre_tour}"
    
