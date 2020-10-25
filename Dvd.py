from Produto import Produto

class  Dvd(Produto):
    def __init__(self,diretor='', duracao=0,  nome='', preco=0):
        super().__init__(nome, preco)
        self._diretor = diretor
        self._duracao = duracao

    @property
    def diretor(self):
        return self._diretor

    @diretor.setter
    def diretor(self,  diretor):
        self._diretor = diretor

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self,  duracao):
        self._duracao = duracao

    def Descricao(self):
        return "[Nome: ] "  + str(self.nome) + " [Preco: ] " + str(self.preco) + " [Preco a vista: ] " + self.getPrecoAvista() + " [Diretor: ] " + str(self.diretor)  + " [Duracao: ] " +str(self.duracao) 
