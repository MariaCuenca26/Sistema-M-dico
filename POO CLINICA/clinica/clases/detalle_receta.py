from clases.base import ModeloBase


class DetalleReceta(ModeloBase):
    """docstring for DetalleReceta."""
    _secuencia = 0
    def __init__(self,  medicamento, cantidad, dosis, duracion, fecuencia):
        DetalleReceta._secuencia += 1
        self.__codigo = DetalleReceta._secuencia
        self.medicamento = medicamento
        self.cantidad = cantidad
        self.dosis = dosis
        self.duracion = duracion
        self.fecuencia = fecuencia
        super(DetalleReceta, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s;%s;%s;%s;%s' %(self.codigo, 
                                   self.medicamento.nombre, 
                                   self.cantidad, 
                                   self.dosis, 
                                   self.fecuencia, 
                                   self.duracion)