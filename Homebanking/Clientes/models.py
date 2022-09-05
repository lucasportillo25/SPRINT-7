from django.db import models

# Create your models here.

class Cliente(models.Model):
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    dni = models.IntegerField(verbose_name='DNI')
    fechanacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    telefono = models.IntegerField(verbose_name='telefono')
    email = models.EmailField(max_length=255, verbose_name='Email')

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        db_table = 'cliente'

    def __str__(self):
        return self.Apellido