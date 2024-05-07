from producto import producto
class tienda:
    #Atributos
    
    __producto1 = None
    __producto2 = None
    __producto3 = None
    __producto4 = None
    __dinero_en_caja = 0
    
    def __init__(self):
        self.__producto1 = producto("PAPELERIA", "LAPIZ", 550,30 ,9)
        self.__producto2 = producto("PAPELERIA", "BORRADOR", 300, 15, 5)
        self.__producto3 = producto("SUPERMERCADO", "CAFE", 5600, 20, 10)
        self.__producto4 = producto("DROGUERIA","DESINFECTANTE", 3200, 12, 11)
        self.__dinero_en_caja = 0
        
    
    #Metodos get
    
    def getproducto1(self):
        return self.__producto1
    
    def vender_cantidad_productos(self, p_nombre, cantidad):
        if producto.__nombre == p_nombre:
            producto.__cantidad_bodega -= cantidad
            return cantidad
        else:
            return "EL producto no existe"
        
    def vender_producto(self,p_nombre, cantidad):
        if producto.__nombre == p_nombre:
           producto.vender(cantidad)
        else:
            print("El producto no existe")
            
    def dar_precio_producto(self,p_numero_productos):
        if p_numero_productos == 1:
            print(self.__producto3.__valor_unitario)
        elif p_numero_productos == 2:
            print(self.__producto2.__valor_unitario)
        elif p_numero_productos == 3:
            print(self.__producto3.__valor_unitario)
        elif p_numero_productos == 4:
            print(self.__producto4.__valor_unitario)            
        else:
            print("No hay mas productos")            
    
                
    def dar_precio_producto_nombre(self,p_nombre_producto):
        if p_nombre_producto == "LAPIZ":
            print(self.__producto1.__valor_unitario)
        elif p_nombre_producto == "BORRADOR":
            print(self.__producto2.__valor_unitario)    
        elif p_nombre_producto == "CAFE":
            print(self.__producto3.__valor_unitario)                
        elif p_nombre_producto == "DESINFECTANTE":
            print(self.__producto4.__valor_unitario)      
        else:
            print("No exisite el producto")      
                    
            
       

       

       
       

                        
    
    
    