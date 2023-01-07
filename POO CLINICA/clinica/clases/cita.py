from clases.base import ModeloBase


class Cita(ModeloBase):
    """docstring for Cita."""
    ESTADOS = (
        (1,'Pendiente'),
        (2,'En curso'),
        (3,'Finalizada'),
        )
    _secuencia = 0
    def __init__(self, paciente, empleado, fecha, hora_inicio, hora_fin, estado=1):
        Cita._secuencia += 1
        self.__codigo = Cita._secuencia
        self.paciente = paciente
        self.empleado = empleado
        self.fecha = fecha
        self.hora_inicio = hora_inicio #datetime.strptime(hora_inicio, '%H:%M %p').time()
        self.hora_fin = hora_fin #datetime.strptime(hora_fin, '%H:%M %p').time()
        self.estado = estado
        super(Cita, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo
    
    def estado_mostrar(self):
        return dict(self.ESTADOS)[self.estado]

    def mostrar(self):
        return u'%s;%s;%s;%s;%s;%s;%s' %(self.codigo, 
                                      self.paciente.nombre_completo_inverso(), 
                                      self.empleado.nombre_completo_inverso(),
                                      self.fecha, 
                                      self.hora_inicio, 
                                      self.hora_fin, 
                                      self.estado_mostrar())