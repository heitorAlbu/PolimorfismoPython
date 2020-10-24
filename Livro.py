from Produto import Produto

class Livro(Produto):
    
    def __init__(self,autor='', editora='', nome='', preco=0):
        super().__init__(nome, preco)
        self._autor = autor
        self._editora = editora

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    
    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, editora):
        self._editora = editora

    def Descricao(self):
        return "O produto é : "  + str(self.nome) + " e custa R$ " + str(self.preco) + " preço a vista : " + self.getPrecoAvista()  + " autor : " + self.autor + " editora : " + self.editora
