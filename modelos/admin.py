from django.contrib import admin
from .models import Empleado, Horario, Asistencia

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puesto', 'fecha_nacimiento', 'genero', 'dni')
    # Otros campos que desees mostrar en la lista de empleados

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'dia_semana', 'hora_entrada', 'hora_salida_almuerzo', 'hora_entrada_almuerzo', 'hora_salida')
    # Otros campos que desees mostrar en la lista de horarios

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha', 'hora_entrada', 'hora_salida_almuerzo', 'hora_entrada_almuerzo', 'hora_salida')
    # Otros campos que desees mostrar en la lista de asistencias
