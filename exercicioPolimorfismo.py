from Produto import Produto
from Cd import Cd
from Dvd import Dvd
from Livro import Livro
import os


#MAIN --------
produto = Produto("cafe", 30)
cd = Cd("Gilberto Gil", "Arnaldo",  "Gil - acústico", 50)
dvd = Dvd("Titanic", 120 ,"Filme - Titanic",90)
livro = Livro("robert", "companhia das letras","livro - '1989", 110)
list = [produto, dvd, cd, livro]

def menuInicial():
    os.system("cls")
    print("Escolha a opção : ")
    print("1) - Listar todos os produtos ")
    print("2) - Cadastrar um novo produto ")
    print("3) - Deletar um produto ")
    print("4) - Atualizar um produto ")
    print("5) - Sair ")
    escolha = int(input())
    return escolha 

def verificarIdExistente(id):
    for item in list:
        if(item.id == int(id)):
            return True
    return False

def cadastrar(tipoProduto):
    try:
        if(str.lower(tipoProduto) == "produto"):
            os.system("cls")
            print("cadastrar um novo produto ")
            print("digite um Nome para o novo produto : ")
            nome = str(input())
            os.system("cls")
            print("digite um Preço para o novo produto : ")
            preco = int(input())
            novoProduto = Produto(nome, preco)
            existeId = verificarIdExistente(novoProduto.id)
            if(existeId == False and  novoProduto.nome != '' and (novoProduto.preco != 0 or novoProduto.preco is not null)):
                list.append(novoProduto)
            elif(existeId == True or (novoProduto.nome == '' or ( novoProduto.preco == 0 or novoProduto is null))):
                raise Exception("Desculpe, não foi possível adicionar o produto")
         

        elif(str.lower(tipoProduto) == "cd"):
            os.system("cls")
            print("cadastrar um novo Cd ")
            print("digite um Nome para o novo Cd : ")
            nome = str(input())
            os.system("cls")
            print("digite um Preço para o novo Cd : ")
            preco = int(input())
            os.system("cls")
            print("digite um Cantor para o novo Cd : ")
            cantor = input()
            os.system("cls")
            print("digite um Produtor para o novo Cd : ")
            produtor = input()
            novoCd = Cd(cantor, produtor, nome, preco)
            existeId = verificarIdExistente(novoCd.id)
            if(existeId == False and  novoCd.nome != '' and (novoCd.preco != 0 or novoCd.preco is not null)):
                list.append(novoCd)
            elif(existeId == True or (novoCd.nome == '' or novoCd.preco == 0 or novoCd.cantor =='' or novoCd.produtor =='')):
                raise Exception ("Desculpe, não foi possível adicionar o produto")

        elif(str.lower(tipoProduto) == "dvd"):
            os.system("cls")
            print("cadastrar um novo Dvd ")
            print("digite um Nome para o novo Dvd : ")
            nome = str(input())
            os.system("cls")
            print("digite um Preço para o novo Dvd : ")
            preco = int(input())
            os.system("cls")
            print("digite um Diretor para o novo Dvd : ")
            diretor = input()
            os.system("cls")
            print("digite a duração para o novo Dvd : ")
            duracao = int(input())
            novoDvd = Dvd(diretor, duracao, nome, preco)
            existeId = verificarIdExistente(novoDvd.id)
            if(existeId == False and  novoDvd.nome != '' and (novoDvd.preco != 0 or novoDvd.preco is not null)):
                list.append(novoDvd)
            elif(existeId == True or (novoDvd.nome == '' or novoDvd.preco == 0 or novoDvd.diretor =='' or novoDvd.duracao !=0)):
                raise Exception ("Desculpe, não foi possível adicionar o produto")
        
        elif(str.lower(tipoProduto) == "livro"):
            os.system("cls")
            print("cadastrar um novo Livro ")
            print("digite um Nome para o novo Livro : ")
            nome = str(input())
            os.system("cls")
            print("digite um Preço para o novo Livro : ")
            preco = int(input())
            os.system("cls")
            print("digite um Autor para o novo Livro : ")
            autor = input()
            os.system("cls")
            print("digite a Editora para o novo Livro : ")
            editora = input()
            novoLivro = Dvd(autor, editora, nome, preco)
            existeId = verificarIdExistente(novoLivro.id)
            if(existeId == False and  novoLivro.nome != '' and (novoLivro.preco != 0 or novoLivro.preco is not null)):
                list.append(novoLivro)
            elif(existeId == True or (novoLivro.nome == '' or novoLivro.preco == '' or novoLivro.autor =='' or novoLivro.editora == '')):
                raise Exception ("Desculpe, não foi possível adicionar o produto")
        else:
            print("Opção inválida !")
    except Exception as erro:
        print(erro)
    finally:
        input()


try:
    escolha = menuInicial()

    while escolha > 0 :
        if(escolha == 1):
            for item in list:
                print(item.Descricao())
            input()
            escolha = menuInicial()
        if(escolha == 2):
            print("que tipo de produto você quer cadastrar ?")
            tipoProduto = input()
            cadastrar(tipoProduto)
            escolha = menuInicial()
        if(escolha == 3):
            pass #Implementar
        if(escolha == 4):
            pass #Implementar
        if(escolha == 5):
            break

except Exception as erro:
    print(erro)
#else:

#finally:

print("FINALIZANDO...")











