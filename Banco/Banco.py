class Banco:
    def __init__(self, id,agencias):
        self.id = id
        self.agencias = agencias 
        self.clientes = []
        self.contas = []

    def listarAgencias(self):
        for agencia in self.agencias:
            print(agencia)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente, conta):
        if conta not in self.contas:
            print("Conta não é deste banco.")
            return False
        if cliente not in self.clientes:
            print("Cliente não é deste banco.")
            return False
        if conta.cliente != cliente:
            print("Esta conta não pertence a este cliente.")
            return False
        if conta.agencia not in self.agencias:
            print("Agência inválida.")
            return False
        print("Autenticação bem-sucedida.")
        return True
