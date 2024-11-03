from abc import ABC, abstractmethod
# Classe abstrata que representa uma conta bancária
class Conta(ABC):
    def __init__(self, saldo: float = 0.0):
        self._saldo = saldo  # Saldo inicial da conta
        self._extrato = Extrato()  # Extrato para registrar as transações

    @abstractmethod
    def depositar(self, valor: float):
        pass  # Método para depositar dinheiro na conta

    @abstractmethod
    def sacar(self, valor: float):
        pass  # Método para sacar dinheiro da conta

    @abstractmethod
    def transferir(self, conta_destino, valor: float):
        pass  # Método para transferir dinheiro para outra conta

    def consultar_saldo(self):
        return self._saldo  # Retorna o saldo atual da conta

# Conta Corrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, saldo: float = 0.0):
        super().__init__(saldo)  # Chama o construtor da classe Conta

    def depositar(self, valor: float):
        self._saldo += valor  # Adiciona o valor ao saldo
        self._extrato.adicionar_transacao("Depósito", valor)  # Registra a transação

    def sacar(self, valor: float):
        if valor <= self._saldo:
            self._saldo -= valor  # Deduz o valor do saldo
            self._extrato.adicionar_transacao("Saque", valor)  # Registra a transação
        else:
            print("Saldo insuficiente.")  # Informa que não tem saldo suficiente

    def transferir(self, conta_destino, valor: float):
        if valor <= self._saldo:
            self._saldo -= valor  # Reduz o valor do saldo
            conta_destino.depositar(valor)  # Vai pra outra conta
            self._extrato.adicionar_transacao("Transferência", valor)  # Registra a transação
        else:
            print("Saldo insuficiente.")  # Informa que não tem saldo suficiente

# Conta Poupança, também herda de Conta
class ContaPoupanca(Conta):
    def __init__(self, saldo: float = 0.0):
        super().__init__(saldo)  # Chama o construtor da classe Conta

    def depositar(self, valor: float):
        self._saldo += valor  # Adiciona o valor ao saldo
        self._extrato.adicionar_transacao("Depósito", valor)  # Registra a transação

    def sacar(self, valor: float):
        if self._saldo - valor >= 99: #Só é possível sacar acima de 100
            self._saldo -= valor  # Reduz o valor do saldo
            self._extrato.adicionar_transacao("Saque", valor)  # Registra a transação
        else:
            print("Saldo insuficiente ou abaixo do mínimo permitido.")  # Informa sobre saldo insuficiente
    
    def transferir(self, conta_destino, valor: float):
        if valor <= self._saldo:
            self._saldo -= valor  # Reduz o valor do saldo
            conta_destino.depositar(valor)  # Vai pra outra conta
            self._extrato.adicionar_transacao("Transferência", valor)  # Registra a transação
        else:
            print("Saldo insuficiente.")  # Informa que não tem saldo suficiente

# Representa um cliente do banco
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self._nome = nome  # Nome do cliente
        self._cpf = cpf  # CPF do cliente
        self._contas = []  # Lista de contas do cliente

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)  # Adiciona uma conta na lista do cliente

    def remover_conta(self, conta: Conta):
        self._contas.remove(conta)  # Remove uma conta da lista do cliente

    def get_nome(self):
        return self._nome  # Retorna o nome do cliente

    def get_cpf(self):
        return self._cpf  # Retorna o CPF do cliente

    def get_contas(self):
        return self._contas  # Retorna todas as contas do cliente

# Classe para gerenciar o extrato de transações
class Extrato:
    def __init__(self):
        self._transacoes = []  # Lista de transações

    def adicionar_transacao(self, descricao: str, valor: float):
        self._transacoes.append(f"{descricao}: R$ {valor:.2f}")  # Adiciona uma transação formatada

    def consultar_extrato(self):
        return self._transacoes  # Retorna todas as transações

# Classe que representa o banco e gerencia os clientes
class Banco:
    def __init__(self):
        self._clientes = []  # Lista de clientes do banco

    def adicionar_cliente(self, cliente: Cliente):
        self._clientes.append(cliente)  # Adiciona um cliente na lista

    def remover_cliente(self, cpf: str):
        for cliente in self._clientes:
            if cliente.get_cpf() == cpf:
                self._clientes.remove(cliente)  # Remove o cliente da lista
                print(f"Cliente {cliente.get_nome()} removido com sucesso.")
                return
        print("Cliente não encontrado.")  # Informa que o cliente não foi encontrado

    def obter_cliente(self, cpf: str):
        for cliente in self._clientes:
            if cliente.get_cpf() == cpf:
                return cliente  # Retorna o cliente encontrado
        return None  # Se não encontrar, retorna None