from Produto import Produto

class Cd(Produto):

    def __init__(self, cantor='', produtor='', nome='', preco = 0):
            super().__init__(nome,preco)
            self._cantor = cantor
            self._produtor = produtor

    @property
    def cantor(self):
        return self._cantor

    @cantor.setter
    def cantor(self, cantor):
        self._cantor = cantor

    @property
    def produtor(self):
        return self._produtor

    @produtor.setter
    def produtor(self, produtor):
        self._produtor = produtor

    def Descricao(self):
        return "[Nome: ] "  + str(self.nome) + " [Preco: ] " + str(self.preco) + " [Preco a vista: ] " + self.getPrecoAvista() +" [Cantor: ] " + self.cantor + " [Produtor :] " + self.produtor
