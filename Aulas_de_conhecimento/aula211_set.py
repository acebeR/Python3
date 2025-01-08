class Conexao:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.senha = None

    def set_user(self, user):
        self.user = user

    def set_senha(self, senha):
        self.senha = senha

    @classmethod
    def criar_com_auth(cls,user,senha):
        conexao = cls()
        conexao.user = user
        conexao.senha = senha
        return conexao


c1 = Conexao.criar_com_auth('Rebeca','teste')
print(c1.user)

