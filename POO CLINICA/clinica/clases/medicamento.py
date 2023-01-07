from clases.base import ModeloBase


class Medicamento(ModeloBase):
    """docstring for Medicamento."""
    _secuencia = 0
    def __init__(self, nombre):
        Medicamento._secuencia += 1
        self.__codigo = Medicamento._secuencia
        self.nombre = nombre
        super(Medicamento, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s' %(self.codigo, self.nombre)