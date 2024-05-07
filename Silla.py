class Silla:

    CLASE = {
        'eje':'Ejecutiva',
        'eco':'Econimica'
    }

    UBICACION = {
        'ventana':'Ventana',
        'centro':'Centro',
        'pasillo':'Pasillo'
    }

    def __init__(self, p_numero, p_clase, p_ubicacion):
        self.__numero = p_numero
        self.__clase = (self.CLASE.eje, self.CLASE.eco)[p_clase]
        if p_ubicacion is 'ventana':
            self.__ubicacion = self.UBICACION.ventana
        elif p_ubicacion is 'centro':
            self.__ubicacion = self.UBICACION.centro
        elif p_ubicacion is 'pasillo':
            self.__ubicacion = self.UBICACION.pasillo
        else:
            self.__ubicacion = None
        self.__pasajero = None


    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero
        
    def desasignarpasajero(self):
        self.__numero = None

    def sillaAsignada(self):
        return True if self.__numero is None else False
    
    def getNumero(self):
        return self.__numero
    
    def getClase(self):
        return self.__clase
    
    def getUbicacion(self):
        return self.__ubicacion
    
    def getPasajero(self):
        return self.__pasajero