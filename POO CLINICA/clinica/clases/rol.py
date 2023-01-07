from clases.base import ModeloBase


class Rol(ModeloBase):
    """docstring for Rol."""
    _secuencia = 0
    def __init__(self, nombre):
        Rol._secuencia += 1
        self.__codigo  = Rol._secuencia
        self.nombre = nombre
        super(Rol, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s' %(self.codigo, self.nombre)  