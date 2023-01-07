from clases.base import ModeloBase


class Usuario(ModeloBase):
    
    """docstring for Usuario."""
    _secuencia  = 0
    def __init__(self, nombre_usuario, clave):
        Usuario._secuencia += 1
        self.__codigo = Usuario._secuencia 
        self.nombre_usuario = nombre_usuario
        self.__clave = clave
        super(Usuario, self).__init__()
    
    @property
    def codigo(self):
        return self.__codigo
        
    @property
    def clave(self):
        return self.__clave
        
    def mostrar(self,):
        return '%s;%s' %(self.codigo, self.nombre_usuario)
