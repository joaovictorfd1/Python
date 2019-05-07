class Grafo:
    def __init__(self, dicionario=None):
        if dicionario is None:
            dicionario = [] 
        self.dicionario = dicionario
    def listarVetices (self):
        return list(self.dicionario.keys())
    def listarArestas(self):
        return list(self.dicionario.values())
    def addVertice(self, vertice):
        if vertice not in self.dicionario:
           self.dicionario[vertice] = []
    def addAresta(self, vertice, aresta):
        array = self.dicionario.get(vertice)
        array.append(aresta)
        self.dicionario[vertice] = array
    def removerVertice(self, vertice):
        if vertice in self.dicionario:
            self.dicionario.pop(vertice)
    def removerAresta(self, vertice, aresta):
         array = self.dicionario.get(vertice)
         for i in array:
             if i == aresta:
                 array.remove(i)
            

dic = {'A': ['B', 'C', 'E'],
       'B': ['A','D', 'E'],
       'C': ['A', 'F', 'G'],
       'D': ['B'],
       'E': ['A', 'B','D'],
       'F': ['C'],
       'G': ['C']}

g = Grafo(dic)


#g.addVertice('H')

g.addVertice('Michel')
g.addAresta('Michel', 'A')
g.addAresta('Michel', 'B')
g.addAresta('Michel', 'C')
g.addAresta('Michel', 'D')
g.addAresta('Michel', 'E')
g.addAresta('Michel', 'F')
g.addAresta('Michel', 'G')
g.addAresta('Michel', 'Michel')

#g.addAresta('H','A')
#g.addAresta('H','B')
#g.addAresta('H','H')

#g.removerAresta('H','A')
#g.removerAresta('H','B')
#g.removerVertice('A')



#print(dic)
#g.listarArestas()
#print(g.listarArestas())
g.removerAresta('Michel', 'Michel')
#g.removerVertice('Michel')
print(dic)
#g.listarArestas()
#print(g.listarArestas())