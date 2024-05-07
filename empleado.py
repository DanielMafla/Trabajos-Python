from fecha import Fecha

class Empleado:
    #Aqui va el codigo del empleado
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    nombre = ''
    apellido = ''
    Numero_de_hijos = 2
    
    '''----------------------------------------------------------------
    # 1 = Masculino y 2 = Femenino
    ----------------------------------------------------------------'''
    sexo= 1
    salario = 0
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def __init__(self, nombre, apellido, sexo, salario,Numero_de_hijos):
        self.nombre = nombre
        self.apellido =apellido
        self.sexo = sexo
        self.salario = salario
        self.Numero_de_hijos = Numero_de_hijos
    
    def CambiarSalario(self, nuevoSalario):
        # Aqui va el codigo del metodo
        self.salario = nuevoSalario
        return 'El salario se ha actualizado '+self.salario
        
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va el codigo del nuevo empleado
        return None
    
    def Consultar_sexo(self):
        return self.sexo
    
    
    def ConsultarSalario(self):
        # Aqui va el codigo del metodo
        return self.salario
    
    def ConsultarNombre(self):
        return self.nombre
    
    def ConsultarApellido(self):
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        return self.nombre +" "+ self.apellido
    
    def AumentoSalarial(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario
        return "El nuevo salario es de: "+self.salario
    
    def CambiarNombre(self, nNombre):
        self.nombre = nNombre
        return "El nuevo nombre es "+self.nombre
    
    def CambiarApellido(self,nApellido):
        self.apellido= nApellido
        return "El nuevo apellido es "+self.apellido 
    
    def DuplicarSalario(self):
        # Aqui va el codigo
        # Forma 1
        # self.salario = self.salario*2
        # Forma 2 pro
        self.salario *= 2
        
    def CalcularSalarioAnual(self):
        # Aqui va el codigo
        # Forma 1
        salarioAnual = self.salario*12
        return salarioAnual
        # Forma 2
        # return self.salario*12
    
    def ConsultarDiaCumpleanios(self):
        return "El dia de su cumpleaños es: "+self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):
        #forma 1
        total = self.CalcularSalarioAnual()
        return (total * 19.5) / 100 
        #forma 2
        #return self.CalcularSalarioAnual() * 0.195
        
    def Numero_hijos(self):
         return "La cantidad de hijos es: "+self.Numero_de_hijos
     
    def Auxilio_educativo(self):
        Auxilio = (self.salario * 5)/ 100
        Auxilio = Auxilio * self.Numero_de_hijos
        return "El auxilio educativo es de: "+ Auxilio
    
    def Auxilio_educativo_parametro(self,Porcentaje):
        Auxilio = (self.salario * Porcentaje) / 100
        Auxilio = Auxilio * self.Numero_de_hijos
        return "El auxilio sera de: "+ Auxilio
    
    def Diferencia_salarios(self,Salario_empleado2):
        Diferencia = self.salario - Salario_empleado2
        return "La diferencia entre los salarios es: "+ Diferencia
    
    
                    
    
    
        
        
    
    
        
     
     
     
     
     
     
     
    
    
   
    
    
    
                






    