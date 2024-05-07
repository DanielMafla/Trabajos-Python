from Cuentacorriente import CuentaCorriente
from cuentaahorros import CuentaAhorros
        
class SimuladorBancario:
    
    cedula=''
    nombres=''
    mesActual=''
    
    #2 = VIP   /  1 = Platino   /   0 = Normal
    
    Tipo_cliente = 2
    
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    
    corriente = CuentaCorriente()
    ahorros = CuentaAhorros()
    
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def __init__(self,cedula,nombres,mesActual,Tipo_cliente):
        self.cedula = cedula
        self.nombres = nombres
        self.mesActual = mesActual
        self.Tipo_cliente = Tipo_cliente
        
        
        
    def Consultar_cedula(self):
         return "Tu cedula es: "+ self.cedula
        
        
    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0
        
    def ConsultarSaldoCorriente(self):
        return "Tu saldo es: "+self.corriente.ConsultarSaldo()
    
    def DuplicarAhorro(self):
        #forma 1
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo())
        
        # # Forma 2
        # self.ahorros.saldo *= 2
    
    def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.corriente.RetirarMonto(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        return "Retiraste total: "+total
    
    def Consultar_tipo_cliente(self):
        return "La clase de cliente es: "+ self.Tipo_cliente
    
    def Cambiar_tipo_cliente(self,Nuevo_tipo_cliente):
        
        Ntipo = self.Tipo_cliente = Nuevo_tipo_cliente
        
        return "Se actualizo eñ tipo de cliente a: "+ Ntipo
    
    
    
    
    
    
    
    
    
    
         
        
    
    
