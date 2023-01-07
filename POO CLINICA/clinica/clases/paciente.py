from clases.empleado import Empleado
from clases.persona import Persona

class Paciente(Persona):
    """docstring for Paciente."""
    _secuencia = 0
    def __init__(self, nombres, apellido_paterno, apellido_materno, cedula, fecha_nacimiento, genero, direccion ):
        Persona._secuencia = Paciente._secuencia
        Paciente._secuencia += 1
        super(Paciente, self).__init__(nombres, apellido_paterno, apellido_materno, cedula, fecha_nacimiento, genero, direccion)