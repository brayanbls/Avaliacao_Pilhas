from LivRev import Revista, Livro

def menu():
    valor = 0
    revista = Revista()
    livro = Livro()

    while valor != 7:
        print("""
        1 - Adicionar Revista
        2 - Remover Revista
        3 - Lista de Revistas
        4 - Adicionar Livro
        5 - Remover Livro
        6 - Lista de livros
        7 - Sair
        """)

        valor = int(input("Digite a opção desejada: "))

        if valor == 1:
            idRevista = int(input("Digite o id da revista: "))
            dataRevista = input("Digite a data de publicação: ")
            precoRevista = int(input("Digite o preço da revista: "))
            revista.adicionar(idRevista, dataRevista, precoRevista)
        if valor == 2:
            revista.remover()
        if valor == 3:
            revista.imprimir()
        if valor == 4:
            idLivro = int(input("Digite o id do Livro: "))
            dataLivro = input("Digite a data de publicação: ")
            tituloLivro = input("Digite o titulo do livro: ")
            autorLivro = input("Digite o autor do livro: ")
            livro.adicionar(idLivro, dataLivro, tituloLivro, autorLivro)
        if valor == 5:
            livro.remover()
        if valor == 6:
            livro.imprimir()
        if valor == 7:
            pass
        if valor > 7:
            print("Opção inválida")
    print("Fim do programa")

menu()
