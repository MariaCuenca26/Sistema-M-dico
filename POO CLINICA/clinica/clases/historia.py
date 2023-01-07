
from clases.base import ModeloBase
from clases.detalle_historia import DetalleHistoria


class Historia(ModeloBase):
    """docstring for Historia."""
    _secuencia = 0
    def __init__(self, paciente, fecha, notas_internas):
        Historia._secuencia += 1
        self.__codigo = Historia._secuencia
        self.paciente = paciente
        self.fecha = fecha 
        self.notas_internas = notas_internas
        self.antecedentes = []
        super(Historia, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo
    
        
    @property
    def numero(self):
        return 'COD-HIST-%s'%(self.__codigo)

    def mostrar(self):
        return u'%s;%s;%s;%s;%s' %(self.codigo, 
                                self.paciente.nombre_completo_inverso(),
                                self.numero,
                                self.fecha, 
                                self.notas_internas)
    
    def agregar_detallehistoria(self, antecedente, descripcion):
        detalle = DetalleHistoria(antecedente, descripcion)
        self.antecedentes.append(detalle)