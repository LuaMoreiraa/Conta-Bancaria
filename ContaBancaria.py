class ContaBancaria:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}')
        else:
            print('Saldo insuficiente.')

conta_joao = ContaBancaria('João', saldo=1000)
conta_joao.depositar(500)
conta_joao.sacar(200)
