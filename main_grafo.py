#Grafo em Python
#from classe import Grafo

grafo_pai = {"A":["B"], "B":["A"], "C":["D"], "D":["C"]}
#for x in grafo:
#    print(grafo[x])
class Grafo:

    def getlistar(self,grafo_pai):
        for x in grafo_pai:
            print (x, grafo_pai[x])

    def getadd_grafo(self,vertice,aresta,grafo_pai):
        grafo_pai[vertice] = [aresta]

    def getadd_vertice(self,novo,grafo_pai):
        grafo_pai[novo] = []

    def getadd_aresta(self,vertice, aresta, grafo_pai):
        grafo_pai[vertice] = [aresta]

    def getdel(self,vertice,grafo_pai):
        del(grafo_pai[vertice])

    
#print("Listando os Vertices e as Arestas que fazem ligação")
#Grafo.getlistar(Grafo, grafo_pai)
#print("Adicionando um novo Grafo, com Vertice E e que liga a aresta A")
#Grafo.getadd_grafo(Grafo, "E", "A", grafo_pai)
#print("Criando um novo Vertice sem ligação com nenhuma aresta")
#Grafo.getadd_vertice(Grafo, "E", grafo_pai)
#print("Deletando um Vertice")
#Grafo.getdel(Grafo,"A",grafo_pai)
print("Adicionando uma aresta a um vertice existente")
Grafo.getadd_aresta(Grafo,"A","D",grafo_pai)
Grafo.getlistar(Grafo, grafo_pai)