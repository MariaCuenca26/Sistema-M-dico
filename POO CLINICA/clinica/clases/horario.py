from datetime import datetime
import time 
from clases.base import ModeloBase


class Horario(ModeloBase):
    """docstring for Horario."""
    DIAS = (
        ('Lu', 'Lunes'),
        ('Ma', 'Martes'),
        ('Mi', 'Miercoles'),
        ('Ju', 'Jueves'),
        ('Vi', 'Viernes'),
        ('Sa', 'Sabado'),
        ('Do', 'Domingo'),
    )
    _secuencia = 0
    def __init__(self, dia, hora_inicio, hora_fin):
        Horario._secuencia += 1
        self.__codigo = Horario._secuencia
        self.dia = dia
        self.hora_inicio = hora_inicio #datetime.strptime(hora_inicio, '%H:%M %p').time()
        self.hora_fin = hora_fin #datetime.strptime(hora_fin, '%H:%M %p').time()
        super(Horario, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo
    
    def dia_mostrar(self):
        return dict(self.DIAS)[self.dia]

    def mostrar(self):
        return u'%s;%s;%s;%s' %(self.codigo, self.dia_mostrar(), self.hora_inicio, self.hora_fin)