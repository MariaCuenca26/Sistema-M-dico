from abc import ABC
from clases.persona import Persona


class Empleado(Persona):
    """docstring for Empleado."""
    _secuencia = 0
    def __init__(self, nombres, apellido_paterno, apellido_materno, cedula, fecha_nacimiento, genero, direccion, usuario_acceso, rol, jefe=None):
        Persona._secuencia = Empleado._secuencia
        Empleado._secuencia += 1
        self.jefe = jefe
        self.rol = rol
        self.sueldo = self.calcular_sueldo()
        self.usuario = usuario_acceso
        super(Empleado, self).__init__(nombres, apellido_paterno, apellido_materno, cedula, fecha_nacimiento, genero, direccion)
        
    def calcular_sueldo(self):
        return 0.0
        
    def mostrar(self):
        return '%s;%s' % (super().mostrar(), self.rol.nombre if self.rol else 'Sin Rol Asignado') 