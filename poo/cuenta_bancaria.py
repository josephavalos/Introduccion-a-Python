class CuentaBancaria:

    def __init__(self, num_cuenta, nom_titular, balance):
        """
        Permite asignarles valores
        iniciales a los atributos
        de la cuenta.
        """
        self.num_cuenta = num_cuenta
        self.nom_titular = nom_titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

# Creamos una instancia
mi_cuenta = CuentaBancaria('105-356-865', 'Nora Smith', 5600)

# Para acceder a un atributo de la cuenta
mi_cuenta.generar_balance()

# Depositar dinero
mi_cuenta.depositar(400)
mi_cuenta.generar_balance() # Se actualizo a 6000
