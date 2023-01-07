from datetime import datetime


class ModeloBase(object):
    """docstring for ModeloBase."""
    usuario_creacion = None
    usuario_modificacion = None
    fecha_creacion = datetime.now()
    fecha_modificacion = None
    
    def __init__(self):
        super(ModeloBase, self).__init__()