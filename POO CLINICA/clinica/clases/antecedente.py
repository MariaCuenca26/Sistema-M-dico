from clases.base import ModeloBase


class Antecedente(ModeloBase):
    """docstring for Antecedente."""
    _secuencia = 0
    def __init__(self, nombre, grupo):
        Antecedente._secuencia += 1
        self.__codigo = Antecedente._secuencia
        self.nombre = nombre
        self.grupo = grupo
        super(Antecedente, self).__init__()
        
    @property
    def codigo(self):
        return self.__codigo
    
    def mostrar(self):
        return u'%s;%s;%s' %(self.codigo, self.nombre, self.grupo.nombre)