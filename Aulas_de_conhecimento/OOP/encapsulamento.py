# Encapsulamento (modificadores de acesso:public,protected, private)
# Python Não tem modificadores de acesso
# Mas podemos seguir a seguinte acordo(convenção, pythonico) PEP8
class Foo:
    def __init__(self):
        self.public = 'isso e publico'
        self._protected = 'isso é protegido'
        self.__private = 'não acesso de forma alguma'

    def __metodo_private(self):
        print('Não acesso de forma alguma')
    def _metodo_protected(self):
        print('Acordo entre os programadores de python para não usar fora.')
    def metodo_public(self):
        print('Assim pode usar em qualquer lugar...')


f = Foo()
print(f.public)