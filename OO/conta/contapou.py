from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente: ' + self._saldo)
            return
        
        self._saldo -= valor
        self.detalhes()
        








