from clases.base import ModeloBase

class DetalleHistoria(ModeloBase):
    """docstring for DetalleHistoria."""
    _secuencia = 0
    def __init__(self,  antecedente, descripcion):
        DetalleHistoria._secuencia += 1
        self.__codigo = DetalleHistoria._secuencia
        self.antecedente = antecedente
        self.descripcion = descripcion
        super(DetalleHistoria, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s;%s' %(self.codigo, 
                            self.antecedente.nombre, 
                            self.descripcion)