from clases.horario import Horario
from clases.base import ModeloBase


class Empresa(ModeloBase):
    """docstring for Empresa."""
    _secuencia = 0
    def __init__(self, nombre, ruc, alias='S/N'):
        Empresa._secuencia += 1
        self.__codigo = Empresa._secuencia
        self.nombre = nombre
        self.alias = alias
        self.ruc = ruc
        self.horarios = []
        self.empleados = []
        self.pacientes = []
        super(Empresa, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s;%s;%s' %(self.codigo, self.ruc , self.nombre, self.alias)
    
    
    def agregar_horario(self, dia, hora_inicio, hora_fin):
        horario = Horario(dia, hora_inicio, hora_fin)
        self.horarios.append(horario)
        
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)