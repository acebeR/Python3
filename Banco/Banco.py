class Banco:
    def __init__(self, id,agencias,dataCadastro):
        self.id = id
        self.agencias = agencias 
        self.clientes = []
        self.contas = []
        self.dataCadastro = dataCadastro


    def listarAgencias(self):
        for agencia in self.agencias:
            print(agencia, end='')

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
        
    @classmethod
    def from_dict(cls, dados):
        banco = cls(
            id=dados["id"],
            agencias=dados.get("agencias", [])
        )

        # Reconstruindo objetos Conta
        contas_objetos = []
        for conta_dado in dados.get("contas", []):
            tipo = conta_dado.get("tipo")
            if tipo == "Conta Corrente":
                contas_objetos.append(ContaCorrente.from_dict(conta_dado))
            elif tipo == "Conta Poupança":
                contas_objetos.append(ContaPoupanca.from_dict(conta_dado))
        banco.contas = contas_objetos

        # Se quiser reconstruir os clientes também (opcional)
        banco.clientes = dados.get("clientes", [])

        return banco
