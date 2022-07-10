from Publicacao import Publicacao

class Revista(Publicacao):

    def __init__(self, id=None, dataPub=None, preco=None):
        self.topo = None
        self.tamanho = 0
        super().__init__(id, dataPub)
        self.preco = preco

    def adicionar(self, id,dataPub,preco):
        nodo = Revista(id,dataPub,preco)
        if self.topo == None:
            self.topo = nodo
        else:
            nodo.proximo = self.topo
            self.topo = nodo
        self.tamanho += 1

    def imprimir(self):
        if self.topo == None:
            print("A Pilha está vazia!")
        else:
            print("\n---------------------\n")
            aux = self.topo
            while (aux):
                print(aux.id , ' - ' ,aux.dataPub, ' - ' ,aux.preco,  "\n")
                aux = aux.proximo
            print("Tamanho da Pilha: ", self.tamanho)

    def remover(self):
        if self.topo == None:
            print("A Pilha está vazia!")
        elif self.topo.proximo == None:
            self.topo = None
            self.tamanho = 0
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1


from Publicacao import Publicacao

class Livro(Publicacao):

    def __init__(self, id=None, dataPub=None, titulo=None,autor=None):
        self.topo = None
        self.tamanho = 0
        super().__init__(id, dataPub)
        self.titulo = titulo
        self.autor = autor

    def adicionar(self, id,dataPub,titulo, autor):
        nodo = Livro(id,dataPub,titulo, autor)
        if self.topo == None:
            self.topo = nodo
        else:
            nodo.proximo = self.topo
            self.topo = nodo
        self.tamanho += 1

    def imprimir(self):
        if self.topo == None:
            print("A Pilha está vazia!")
        else:
            print("\n---------------------\n")
            aux = self.topo
            while (aux):
                print(aux.id , ' - ' ,aux.dataPub, ' - ' ,aux.titulo, ' - ', aux.autor,  "\n")
                aux = aux.proximo
            print("Tamanho da Pilha: ", self.tamanho)

    def remover(self):
        if self.topo == None:
            print("A Pilha está vazia!")
        elif self.topo.proximo == None:
            self.topo = None
            self.tamanho = 0
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1