
from clases.base import ModeloBase
from clases.detalle_receta import DetalleReceta


class Receta(ModeloBase):
    """docstring for Receta."""
    _secuencia = 0
    def __init__(self, paciente, motivo, fecha, sintoma, diagnostico, instrucciones):
        Receta._secuencia += 1
        self.__codigo = Receta._secuencia
        self.paciente = paciente
        self.motivo = motivo
        self.fecha = fecha 
        self.sintoma = sintoma
        self.diagnostico = diagnostico
        self.instrucciones = instrucciones
        self.medicamentos  = []
        super(Receta, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo

    def mostrar(self):
        return u'%s;%s;%s;%s;%s;%s' %(self.codigo, 
                                self.paciente.nombre_completo_inverso(), 
                                self.fecha, 
                                self.motivo, 
                                self.sintoma, 
                                self.diagnostico)
    
    def agregar_detallereceta(self, medicamento, cantidad, dosis, duracion, frecuencia):
        detalle = DetalleReceta(medicamento, cantidad, dosis, duracion, frecuencia)
        self.medicamentos.append(detalle) 