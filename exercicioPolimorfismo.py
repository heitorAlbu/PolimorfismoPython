from Produto import Produto
from Cd import Cd
from Dvd import Dvd
from Livro import Livro
import os


#MAIN --------
produto = Produto("cafe", 30)
cd = Cd("Gilberto Gil", "Arnaldo",  "Gil - acústico", 50)
dvd = Dvd("James Cameron", 120 ,"Titanic",90)
livro = Livro("JK Howling,","Editora Rocco","Harry Potter",230)
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
            if(existeId == False and  novoProduto.nome != '' and (novoProduto.preco != 0 or novoProduto.preco is not None)):
                list.append(novoProduto)
            elif(existeId == True or (novoProduto.nome == '' or ( novoProduto.preco == 0 or novoProduto is None))):
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
            if(existeId == False and  novoCd.nome != '' and (novoCd.preco != 0 or novoCd.preco is not None)):
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
            if(existeId == False and  novoDvd.nome != '' and (novoDvd.preco != 0 or novoDvd.preco is not None)):
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
            novoLivro = Livro(autor, editora, nome, preco)
            existeId = verificarIdExistente(novoLivro.id)
            if(existeId == False and  novoLivro.nome != '' and (novoLivro.preco != 0 or novoLivro.preco is not None)):
                list.append(novoLivro)
            elif(existeId == True or (novoLivro.nome == '' or novoLivro.preco == '' or novoLivro.autor =='' or novoLivro.editora == '')):
                raise Exception ("Desculpe, não foi possível adicionar o produto")
        else:
            print("Opção inválida !")
    except Exception as erro:
        print(erro)
    finally:
        input()

def deletar(nomeProduto,tipoProduto):
    for item in list:
        classeOriginal = str(type(item)) #Resgatando a classe original e transformando em String
        classeComparativa = "<class '" + tipoProduto +"." +tipoProduto+"'>" #Traduzindo a classe desejada pro formato
        if(classeOriginal == classeComparativa and item.nome == nomeProduto):
            list.remove(item)
            print("Item deletado com sucesso")


def atualizar(nomeProduto,tipoProduto):
    for item in list:
        classeOriginal = str(type(item)) #Resgatando a classe original e transformando em String
        classeComparativa = "<class '" + tipoProduto +"." +tipoProduto+"'>" #Traduzindo a classe desejada pro formato
        if(classeOriginal == classeComparativa and item.nome == nomeProduto):
            print("Seu objeto possui os seguintes atributos:")
            print(item.Descricao())
            atributo = str.lower(input("Qual atributo deseja alterar:  "))
            valor = input("Digite o dado que será inserido: ")
            if(classeOriginal == "<class 'Dvd.Dvd'>"):
                if(atributo == "nome"):
                    item.nome = valor
                    print("Alterado com Sucesso")
                elif(atributo == "preco"):
                    item.preco == int(valor)
                    print("Alterado com Sucesso")
                elif(atributo == "duracao"):
                    item.duracao = valor
                    print("Alterado com Sucesso")
                elif(atributo == "diretor"):
                    item.diretor = valor
                    print("Alterado com Sucesso")

            elif(classeOriginal == "<class 'Cd.cd'>"):
                if(atributo == "nome"):
                    item.nome = valor
                    print("Alterado com Sucesso")
                elif(atributo == "preco"):
                    item.preco == int(valor)
                    print("Alterado com Sucesso")
                elif(atributo == "cantor"):
                    item.cantor == valor
                    print("Alterado com Sucesso")
                elif(atributo == "produtor"):
                    item.produtor = valor
                    print("Alterado com Sucesso")

            elif(classeOriginal == "<class 'Livro.Livro'>"):
                if(atributo == "nome"):
                    item.nome = valor
                    print("Alterado com Sucesso")
                elif(atributo == "preco"):
                    item.preco == int(valor)
                    print("Alterado com Sucesso")
                elif(atributo == "autor"):
                    item.autor == valor
                    print("Alterado com Sucesso")
                elif(atributo == "editora"):
                    item.editora = valor
                    print("Alterado com Sucesso")

            elif(classeOriginal == "<class 'Produto.Produto'>"):
                if(atributo == "nome"):
                    item.nome = valor
                    print("Alterado com Sucesso")
                elif(atributo == "preco"):
                    item.preco == int(valor)


                
        
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
            tipoProduto = input("Qual o tipo do produto deseja deletar:   ")
            nomeProduto = input("Qual o nome exato do produto:   ")
            deletar(nomeProduto,tipoProduto)
            escolha = menuInicial()
        if(escolha == 4):
            tipoProduto = input("Qual o tipo do produto deseja deletar:   ")
            nomeProduto = input("Qual o nome exato do produto:   ")
            atualizar(nomeProduto,tipoProduto)
            escolha = menuInicial()
        if(escolha == 5):
            break

except Exception as erro:
    print(erro)
#else:

#finally:

print("FINALIZANDO...")











