from Silla import Silla

class Avion:
    SILLAS_EJECUTIVAS = 8 
    SILLAS_ECONIMICAS = 42

    def __init__(self):
        self.sillas_ejecutivas = []
        self.sillas_econimicas = []
        
        self.definicion_sillas_ejecutivas()
        self.definicion_sillas_econimicas()

    def definicion_sillas_ejecutivas(self):
        for i in range(self.SILLAS_EJECUTIVAS):
            if (i+1)%2 == 0:
                self.sillas_ejecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.ventana)
            else:
                self.sillas_ejecutivas.append((i+1), Silla.CLASE.eje, Silla.UBICACION.pasillo)

    def definicion_sillas_econimicas(self):
        for i in range(self.SILLAS_ECONIMICAS):
            contador = 1
            if (i+1) >= 9:
                self.sillas_econimicas.append((i+1), Silla.CLASE.eco, Silla.UBICACION.pasillo)
                contador += 1
                if (i+1) == contador:    
                    self.sillas_econimicas.append((i+1), Silla.CLASE.eco, Silla.UBICACION.centro)
                    contador += 1
                else:    
                    self.sillas_econimicas.append((i+1), Silla.CLASE.eco, Silla.UBICACION.ventana)
                    contador += 1
                if contador == 50:
                    break

    def contar_sillas_ejecutivas_ocupadas(self):
        contador = 0
        for silla in self.sillas_ejecutivas:
            if silla.ocupada:
                contador += 1
        return contador

    def buscar_pasajero_ejecutivo(self, p_cedula):
        for silla in self.sillas_ejecutivas:
            if silla.ocupada and silla.pasajero.cedula == p_cedula:
                return silla
        return None

    def buscar_silla_economica_libre(self, ubicacion):
        for silla in self.sillas_economicas:
            if not silla.ocupada and silla.ubicacion == ubicacion:
                return silla
        return None

    def asignar_silla_economica(self, ubicacion, p_pasajero):
        silla_libre = self.buscar_silla_economica_libre(ubicacion)
        if silla_libre:
            silla_libre.ocupada = True
            silla_libre.pasajero = p_pasajero
            return True
        return False

    def anular_reserva_ejecutivo(self, p_cedula):
        silla = self.buscar_pasajero_ejecutivo(p_cedula)
        if silla:
            silla.ocupada = False
            silla.pasajero = None
            return True
        return False

    def contar_ventanas_economica(self):
        contador = 0
        for silla in self.sillas_economicas:
            if silla.ubicacion == "ventana":
                contador += 1
        return contador

    def hayDosHomonimosEconomica(self):
        nombres = []
        for silla in self.sillas_economicas:
            if silla.ocupada:
                nombre = silla.pasajero.nombre
                if nombre in nombres:
                    return True
                nombres.append(nombre)
        return False



    def contar_sillas_economicas_libres(self):
        sillas_libres = 0
        for fila in self.filas:
            for silla in fila.sillas:
                if silla.clase == "Económica" and not silla.ocupada:
                    sillas_libres += 1
        return sillas_libres

