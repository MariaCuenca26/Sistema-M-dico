from clases.base import ModeloBase


class GrupoAntecedente(ModeloBase):
    """docstring for GrupoAntecedente."""
    _secuencia = 0
    def __init__(self, nombre):
        GrupoAntecedente._secuencia += 1
        self.__codigo = GrupoAntecedente._secuencia
        self.nombre = nombre
        super(GrupoAntecedente, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s' %(self.codigo, self.nombre)