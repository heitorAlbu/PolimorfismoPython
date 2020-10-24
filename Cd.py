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
        return "O produto é : "  + str(self.nome) + " e custa R$ " + str(self.preco) + " -  preço a vista : " + self.getPrecoAvista() +" cantor : " + self.cantor + " produtor : " + self.produtor
