class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas = 0
    
    # Numero de minutos consumidos
    numeroMinutos = 0
    
    # Costo total de las llamadas
    costoLlamadas = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self. numeroLlamadas = 0
        self. numeroMinutos = 0
        self. costoLlamadas = 0

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numeroMinutos

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

  
    def agregarLlamadaLargaDistancia(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380
        
    def agregarLlamadaCelular(self, pMinutos):
        self. numeroLlamadas += 1
        self. numeroMinutos += pMinutos
        self. costoLlamadas += pMinutos * 999


       
