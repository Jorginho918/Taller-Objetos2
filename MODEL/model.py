params = ["account_number", "dni", "name", "balance"]

class CuentaBancaria:
        
    def __init__(self, **kwargs):
        self.account_number = kwargs["account_number"]
        self.dni = kwargs["dni"]
        self.titular_name = kwargs["name"]
        self.balance = kwargs["balance"]
        
    
    def deposit_money(self, deposit):
        retention = deposit * 0.19
        self.balance += deposit - retention
                
    def withdrawals(self, withdrawal: float):
        if withdrawal > self.balance:
            raise ValueError("El retiro excede el saldo disponible")
        else:
            self.balance -= withdrawal
    
    def show_data(self):
        print(f"Numero de cuenta: {self.account_number}")
        print(f"Numero de documento del titular: {self.dni}")
        print(f"Nombre del titular: {self.titular_name}")
        print(f"Saldo disponible: {self.balance}")
        