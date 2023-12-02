from collections import deque
from queue import LifoQueue

class Grafo:
    def __init__(self):
        self.lista_de_adjacencia = {}
        self.lista_de_arestas = []
    
# https://www.geeksforgeeks.org/add-and-remove-edge-in-adjacency-list-representation-of-a-graph/
    def inserirVertice(self, vertice):
        if vertice not in self.lista_de_adjacencia:
            self.lista_de_adjacencia[vertice] = []
    
    def adicionarConexao(self, u, v, peso = 1):
        self.inserirVertice(u)
        self.inserirVertice(v)
        
        self.lista_de_adjacencia[u].append((v, peso))
        self.lista_de_adjacencia[v].append((u, peso))
        
        self.lista_de_arestas.append((u, v, peso))


    def numeroDeVertices(self):
        return len(self.lista_de_adjacencia)
    
    def numeroDeArestas(self):
        return len(self.lista_de_arestas)
    
    def vizinhos(self, vertice):
        return self.lista_de_adjacencia[vertice]
    
    def grauDoVertice(self, vertice):
        return len(self.lista_de_adjacencia[vertice])
    
    def pesoDaAresta(self, u, v):
        for conexao in self.lista_de_adjacencia[u]:
            if conexao[0] == v:
                return conexao[1]

    def menorGrau(self):
        lista = self.lista_de_adjacencia
        return min(len(grau) for grau in lista.values())
    
    def maiorGrau(self):
        lista = self.lista_de_adjacencia
        return max(len(grau) for grau in lista.values())

    def bfs(self, vertice):   
        visitados = set()
        visitados.add(vertice)
        vertices = [vertice]
        pais = [vertice]
        dist = [0]
        
        fila = deque()
        fila.append(vertice)
        
        n = 1
        while(len(fila) != 0):
            v = fila.popleft()
            
            for i in range(len(self.lista_de_adjacencia[v])):
                u = self.lista_de_adjacencia[v][i][0]
                if u not in visitados:
                    print(u)
                    visitados.add(u)
                    vertices.append(u) 
                    pais.append(v)
                    dist.append(n)
                    fila.append(u)
                    n = n + 1 
        
        return vertices, pais, dist
    
    def dfs(self, vertice):
        visitados = set()
        visitados.add(vertice)
        vertices = [vertice]
        pais = [vertice]
        t_inicial, n = [1], 1
        t_final = []
        
        pilha = LifoQueue()
                       
        for i in self.lista_de_adjacencia[vertice]:
            pilha.put(i[0])
                
        while not pilha.empty():
            v = pilha.get()     
            
            if v not in visitados:
                visitados.add(v)
                vertices.append(v)
                
                n = n + 1
                t_inicial.append(n)
                
                for i in self.lista_de_adjacencia[v]:
                    pilha.put(i[0])
                    
            if len(vertices) == self.numeroDeVertices():
                n = n + 1
                t_final.append(n)
            
        for i in range(len(vertices) - 1):
            n = n + 1
            pais.append(vertices[i])
            t_final.insert(0, n)
        
        t_final.insert(0, n + 1)
        
        return vertices, pais, t_inicial, t_final
                


grafo = Grafo()
grafo.adicionarConexao(1, 2)
grafo.adicionarConexao(2, 3)
grafo.adicionarConexao(3, 4)
grafo.adicionarConexao(1, 4)
grafo.adicionarConexao(3, 6)
grafo.adicionarConexao(5, 6)
grafo.adicionarConexao(2, 6)
grafo.adicionarConexao(8, 7)
print(grafo.dfs(1))