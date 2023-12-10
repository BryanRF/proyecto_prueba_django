from django.shortcuts import render
from modelos.models import Empleado

def pagina_base(request):
    empleados = Empleado.objects.all()
    return render(request, 'index.html', {'empleados': empleados})
