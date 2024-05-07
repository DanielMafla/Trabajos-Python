class curso:

    __notas = [5.0, 4.3, 3.5, 1.5, 5.0, 1.5, 3.0, 2.0, 5.0, 1.5, 3.0, 2.0]
    
    
    def cantidad_valores (self):
      print(len(self.__notas))
      print(self.__notas[5])
      
    
    def promedio (self):
        suma = 0.0
        indice = 0
        while indice <= 11:
            suma += self.__notas(indice)
            indice+=1
              
        return suma/indice        
    def cantidad_aprobados1(self):
        aprobados = 0
        indice = 0
        while indice<12:
           if(self.__notas(indice))>= 3 and self.__notas(indice)<=5:
               aprobados+=1
           indice +=1
           
         return aprobados
           
    def calcularcantidaaprobados2(self):
        aprobados = 0
        for indice in range(11):
            if(self.__notas[indice])>= 3 and self.__notas[indice]<=5.0:
               aprobados+=1
        return aprobados       
        
        
    def calcularcantidaaprobados3(self):
        aprobados = 0
        for notas in self.__notas:
            if notas >= 3.0 and notas<=5.0:
                aprobados+=1

        return aprobados
    
    def calcular_mayor_nota(self):
        nota_mas_alta = 0
        for indice in range(12):
            if (self.__notas[indice]) < nota_mas_alta:
                nota_mas_alta = self.__notas[indice]
        return nota_mas_alta
    
    def hacer_curva(self):
        indice = 0
        for indice in range(12):
            if (self.__notas[indice])<= 4.76:
                self.__notas += self.__notas[indice] * 0.05
        return self.__notas
    def hay_algun_cinco(self):
        hay_cinco = False
        for i in range(len(self.__notas)):
            if (self.__notas[i] == 5):
               hay_cinco = True
        return hay_cinco



    def hay_algun_cinco_while(self):
        i = 0
        hay_cinco = False
        while(i < len(self.__notas)) and not hay_cinco:
            if(self.__notas[i] == 5):
                hay_cinco = True
                i+=1

        return hay_cinco

    def aumentar_notas(self):
        contador = 0
        for i in range(len(self.__notas)):
            if (self.__notas[i] == 1.5) and contador == 3:
                self.___notas[i] = 2.5
                contador += 1
        return self.__notas            

    def retorna_notas_5(self):
        cantidad_cincos = 0
        for i in range(len(self.__notas)):
            if (self.__notas[i]) == 5.0 and cantidad_cincos < 3:
                cantidad_cincos += 1
            elif cantidad_cincos == 3:
                return 1
        return -1       
    

    
                    