from enum import Enum
#Para crear tipo de clasese enumeradas
#Enumeraciones
class tipo(Enum):
    #Enumeraciones para los tipos de productos
    
    PAPELERIA = 1
    SUPERMERCADO = 2
    DROGUERIA = 3
    
class producto:
    
    # Constantes por el uso de mayusculas y privadas por el __ doble barra baja
    
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.16
    __IVA_DROGUERIA = 0.16
    
    #Atributos
    __nombre = None
    __tipo = Enum("tipo",["PAPELERIA","SUPERMERCADO", "DROGUERIA"])
    __valor_unitario = 0.0
    __cantidad_bodega = 0
    __cantidad_minima = 0
    __cantidad_unidades_vendidas = 0
    
    #Metodos
    
    def __init__(self,tipo , p_nombre,p_valor_unitario, p_cantidad_bodega, p_cantidad_minima):
        self.__tipo=tipo
        self.__nombre=p_nombre
        self.__valor_unitario = p_valor_unitario
        self.__cantidad_bodega = p_cantidad_bodega
        self.__cantidad_minima = p_cantidad_minima
        
        

    def getnombre(self):
        return self.__nombre
    
    def getvalor_unitario(self):
        return self.__valor_unitario
    
    def getcantidad_bodega(self):
        return self.__cantidad_bodega
    
    def getcantidad_minima(self):
        return self.__cantidad_minima
    
    def getcantidad_unidades_vendidas(self):
        return self.__cantidad_unidades_vendidas
    
    def cambiarTipo(self):
        self.__tipo= self.__tipo.SUPERMERCADO
        
    def set_nombre(self, nombre):
        self.__nombre = nombre    
        
    def set_tipo(self, tipo):
        self.__tipo = tipo
    
    def set_valor_unitario (self, valor_unitario):
        self.__valor_unitario = valor_unitario
        
    def set_cantidad_bodega (self, cantidad_bodega):
        self.__cantidad_bodega = cantidad_bodega
        
    def set_cantidad_minima (self, cantidad_minima):
        self.__cantidad_minima = cantidad_minima
        
    def set_cantidad_unidades_vendidas (self, cantidad_unidades_vendidas):
        self.__cantidad_unidades_vendidas = cantidad_unidades_vendidas
    
    def vender(self, cantidad):
        if cantidad <= self.__cantidad_bodega:
            self.set_cantidad_unidades_vendidas += cantidad
            self.__cantidad_bodega -= cantidad     
        else:
            print("Cantidad no disponible")
            
    def hay_suficente(self,cantidad):
        if self.__cantidad_bodega >= cantidad:
            return True
        else:
            return False
        
    def dar_iva(self):
        if self.__tipo=="PAPELERIA":
            return self.__IVA_PAPELERIA
        elif self.__tipo=="FAMRACIa":
            return self.__IVA_DROGUERIA
        elif self.__tipo=="SUPERMERCADO":
            return self.__IVA_SUPERMERCADO
        else:
            print("Categoria de prducto no existe")   
            
    def subir_valor_unitario(self):
        if self.__valor_unitario < 1000: 
            self.__valor_unitario += (self.__valor_unitario * 0.01)
            
        elif self.__valor_unitario > 1000 & self.__valor_unitario < 5000:
            self.__valor_unitario += (self.__valor_unitario * 0.02)       
               
        else:
            self.__valor_unitario += (self.__valor_unitario * 0.03)              
 
    def  hacer_pedido(self, cantidad):
        if self.__cantidad_bodega < self.__cantidad_minima:
            self.__cantidad_bodega + cantidad
        else:
            print("Hay suficiente producto en la bodega")  
    
    def cambiar_valor_unitario(self):
        if tipo.FARMACIA | tipo.PAPELERIA:
            self.__valor_unitario -= (self.__valor_unitario * 0.1)
        elif tipo.SUPERMERCADO:
            self.__valor_unitario += (self.__valor_unitario * 0.5)  
        else:
            print("El tipo de producto no existe") 
            
    def nombre_tipo_producto(self):
        return "El tipo de producto es: "+ self.__tipo
    
    def subir_valor_unitario_tipo(self):
        if  tipo.DROGUERIA:
            self.__valor_unitario *= 0.01
        elif tipo.PAPELERIA:
            self.__valor_unitario *= 0.02
        elif tipo.SUPERMERCADO:
            self.__valor_unitario *= 0.03
        else:
            print("El tipo no eiste")
                        
                    
    
    
                   
            
                
              
            
                
            
            
    
   

    
       
    #6:
       #calcular el numero de productos de papeleria que se venden en la tienda 
       #El metodo se llama "cuantos papeleria"        
        
            
                                        
    
        
        
