import os
import django
import sys

# Agrega la ruta al directorio del proyecto al path de Python
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ruta_proyecto)

# Establecer la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoSinfo.settings')

# Configurar Django
django.setup()


from nominas.models import empleados

class Empleados():
    def getEmpleados():
        listaEmpleados = list(empleados.objects.all().values())
        #lista_de_listas = [[valor for valor in diccionario.values()] for diccionario in listaEmpleados]
        return listaEmpleados

    def get_empleado_by_id(idEmpleado):
        try:
            empleado = empleados.objects.get(id=idEmpleado)
            return empleado
        except empleados.DoesNotExist:
            return None 
        
    def actualizar_empleado(id_empleado, nombre, numero, horas):
        try:
            empleado = empleados.objects.get(id=id_empleado)
            empleado.Nombre = nombre
            empleado.Numero = numero
            empleado.Horas = horas
            empleado.save()
            return True  # Retorna True si se actualizó correctamente
        except empleados.DoesNotExist:
            return False  # Retorna False si el empleado no existe