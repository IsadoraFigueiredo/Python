class Conta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado. Novo saldo: R$ {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado. Novo saldo: R$ {self.saldo}")
        else:
            print("Saldo insuficiente.")

# Instanciando a classe com um saldo inicial de R$ 1000
minha_conta = Conta("João", 1000)

# Realizando operações de depósito e saque
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.sacar(1500)  # Tenta sacar um valor maior que o saldo disponível
