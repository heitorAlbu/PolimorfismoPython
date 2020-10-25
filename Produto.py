import random
class Produto:
    
    def __init__(self ,nome='', preco=0):
        self._id = random.randint(1, 99999)
        self._nome = nome
        self._preco = preco
    
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco
        
    def getPrecoAvista(self):
        return str(self.preco * 0.9)
    
    def Descricao(self):
        return "[Nome: ] "  + str(self.nome) + " [Preco: ] " + str(self.preco) + " [Preco a vista: ] " + self.getPrecoAvista()
    