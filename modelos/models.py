from django.db import models
import uuid
class Empleado(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dni = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return f"{self.nombre} - {self.dni} - {self.puesto}"
    
class Horario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=15)  # Lunes, Martes, etc.
    hora_entrada = models.TimeField()
    hora_salida_almuerzo = models.TimeField()
    hora_entrada_almuerzo = models.TimeField()
    hora_salida = models.TimeField()
    def __str__(self):
        return f"Horario de : {self.empleado.nombre}"

class Asistencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida_almuerzo = models.TimeField()
    hora_entrada_almuerzo = models.TimeField()
    hora_salida = models.TimeField()
    def __str__(self):
        return f"Asistencia de : {self.empleado.nombre} del dia {self.fecha}"
