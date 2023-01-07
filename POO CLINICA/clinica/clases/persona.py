
from datetime import datetime

from clases.base import ModeloBase


class Persona(ModeloBase):
    """docstring for Persona."""
    GENEROS = (
            ('F', 'Femenino'),
            ('M', 'Masculino'),
        )
    _secuencia = 0
    def __init__(self, nombres, apellido_paterno, apellido_materno, cedula, fecha_nacimiento, genero, direccion):
        Persona._secuencia += 1
        self.__codigo = Persona._secuencia
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.cedula = cedula
        self.direccion = direccion
        self.genero = genero
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d-%m-%Y').date()
        super(Persona, self).__init__()
    
    def __str__(self):
        return self.nombres
    
    @property
    def codigo(self):
        return self.__codigo
    
    def nombre_completo(self):
        return u'%s %s %s' % (self.nombres, self.apellido_paterno, self.apellido_materno)
    
    def nombre_completo_inverso(self):
        return u'%s %s %s' % (self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def edad(self):
        fecha_actual = datetime.now().date()
        return fecha_actual.year - self.fecha_nacimiento.year
    
    def genero_mostrar(self):
        return dict(self.GENEROS)[self.genero]
    
    def mostrar(self):
        return u'%s;%s;%s;%s;%s;%s' % (self.codigo, self.cedula, self.nombre_completo(), self.genero_mostrar(), self.direccion, self.fecha_nacimiento)