from collections import deque # biblioteca da fila
from queue import LifoQueue # biblioteca da pilha
import heapq # biblioteca da fila de prioridades

""" 
    Classe que implementa estrura de dados para digrafos, ou seja, grafos direcionados utilizando lista de adjacência
"""

class Digrafo:
    def __init__(self):
        self.lista_de_adjacencia = {} # inicializa a lista de adjacência do grafo
        self.lista_de_arestas = [] # inicializa a lista de arestas do grafo
    
    # insere um vértice no grafo
    def adicionarVertice(self, vertice):
        if vertice not in self.lista_de_adjacencia: # confere se o vértice não está na lista
            self.lista_de_adjacencia[vertice] = [] # insere o vértice na lista
    
    """ 
        adiciona uma aresta no grafo
        tem como parâmetro o vértice de origem e o de destino, e o peso da aresta
        caso não seja ponderada, tem peso = 1
    """
    def adicionarAresta(self, u, v, peso = 1):
        self.adicionarVertice(u)
        self.adicionarVertice(v)
        
        self.lista_de_adjacencia[u].append((v, peso))
        
        self.lista_de_arestas.append((u, v, peso))

    # retorna a quantidade de vértices existente no grafo
    def numeroDeVertices(self):
        return len(self.lista_de_adjacencia)
    
    # retorna a quantidade de arestas existente no grafo
    def numeroDeArestas(self):
        return len(self.lista_de_arestas)
    
    # retorna a vizinhança de um vértice
    def vizinhos(self, vertice):
        return self.lista_de_adjacencia[vertice]
    
    # retorna o grau do vértice
    def grauDoVertice(self, vertice):
        grauDeSaida = len(self.lista_de_adjacencia[vertice]) # calcula qual o grau de saída do vértice
        grauDeEntrada = 0
        
        # calcula o grau de entrada do vértice
        for i in range(self.numeroDeVertices()):
            for tupla in self.lista_de_adjacencia[i+1]: # procura se algum vértice é direcionado ao vértice que queremos o grau
                if tupla[0] == vertice: 
                    grauDeEntrada = grauDeEntrada + 1 # se sim, incrementa o valor do grau de entrada
       
        return grauDeSaida + grauDeEntrada
    
    """ 
        retorna o peso de uma aresta
        tem como parâmetro os vértices que a aresta conecta
    """
    def pesoDaAresta(self, u, v):
        for conexao in self.lista_de_adjacencia[u]: # confere cada vértice que a origem se conecta
            if conexao[0] == v: # se encontrar o vértice correspondente ao destino
                return conexao[1] # retorna o peso dessa aresta

    # retorna o menor grau presente no grafo
    def menorGrau(self):
        lista = self.lista_de_adjacencia
        return min(len(grau) for grau in lista.values()) # procura o menor número de conexões dos vértices, ou seja, o menor número de valores em cada chave
    
    # retorna o maior grau presente no grafo
    def maiorGrau(self):
        lista = self.lista_de_adjacencia
        return max(len(grau) for grau in lista.values()) # procura o maior número de conexões dos vértices,  ou seja, o maior número de valores em cada chave

    # realiza a busca em largura a partir de um determinado vértice
    def bfs(self, vertice):   
        visitados = set() # utiliza um set para verificar quais vértices já foram visitados
        visitados.add(vertice) # adiciona a origem aos visitados
        pais = {vertice : vertice} # inicializa o dicionario que mostra os pais de cada vértice
        dist = {vertice : 0}  # inicializa o dicionario que mostra a distância a partir do vértice de origem até cada novo vértice
        
        fila = deque() # fila que será utilizada para a bfs
        fila.append(vertice) # o primeiro valor da fila será o vértice de origem
        
        while(len(fila) != 0): # agora a busca será realizada enquanto a fila não estiver vazia
            v = fila.popleft() # pega o primeiro valor da fila e o remove
            
            for i in range(len(self.lista_de_adjacencia[v])): 
                u = self.lista_de_adjacencia[v][i][0] # percorre cada vértice vizinho de v
                if u not in visitados: # se esse vertice não tiver sido visitado
                    visitados.add(u) # adiciona aos visitados
                    fila.append(u) # adiciona ele na fila para visitar os vizinhos dele
                    pais[u] = v # adiciona o pai dele, ou seja, v
                    dist[u] = dist[v] + 1 # adiciona a distância dele em relação a origem
        
        return pais, dist
    
    # realiza a busca em profundidade a partir de um determinado vértice
    def dfs(self, vertice):
        visitados = set() # utiliza um set para verificar quais vértices já foram visitados
        visitados.add(vertice) # adiciona o vértice que é a origem
        vertices = [vertice] # inicializa a lista de vértices que mostra a ordem dos vértices que serão visitados
        pais = {vertice : vertice} # inicializa a lista que mostra os pais de cada vértice, na ordem que serão visitados        
        t_inicial = [1] # inicializa a lista que contém o tempo inicial de cada vértice, na ordem que serão visitados
        t_final = [] # inicializa a lista que contém o tempo final de cada vértice, na ordem que serão visitados
        t = 1 # t é o tempo do vértice em relação a origem
        
        pilha = LifoQueue() # inicializa a pilha que será utilizada para fazer a dfs
                       
        for i in self.lista_de_adjacencia[vertice]:
            pilha.put(i[0]) # adiciona na pilha cada vértice que está ligado à origem
            if i[0] not in pais: # caso esse vertice não tenha seu pai declarado
                pais[i[0]] = vertice # declara o pai dele
        
        while not pilha.empty(): # enquanto a pilha não estiver vazia
            v = pilha.get() # pega o vértice do topo da pilha
            
            if v not in visitados: # se o vertice não tiver sido visitado
                visitados.add(v) # adiciona em visitados
                vertices.append(v) # adiciona na lista de vértices, na ordem que foi visitado
                
                t = t + 1 # incremeta o tempo
                t_inicial.append(t) # adiciona o tempo em relação ao vértice que foi visitado
                
                for i in self.lista_de_adjacencia[v]:
                    pilha.put(i[0]) # adiciona na pilha cada vértice que está ligado ao vértice recém-visitado
                    if i[0] not in pais: # caso esse vertice não tenha seu pai declarado
                        pais[i[0]] = v # declara o pai dele

        for i in range(len(vertices) - 1): # aqui declara o tempo final de cada vertice 
            t = t + 1 # incrementa o tempo 
            t_final.insert(0, t) # insere no inicio o tempo , visto que, o ultimo a terminar é o primeiro a ser visitado
        
        t_final.insert(0, t + 1) # insere para o vertice de origem da dfs
        
        return vertices, t_inicial, t_final, pais
    
    # utiliza bellman ford para procurar o caminho mínimo de um vértice para todos os outros do grafo
    def bellman_ford(self, vertice):
        dist = [float("Inf" )] * self.numeroDeVertices() # inicializa uma lista que considera como infinito a distância dos vértices em relação a origem
        dist[vertice - 1] = 0 # define como zero a distância da origem, já que é em relação a ela mesmo
        vertices = [0] * self.numeroDeVertices() # inicializa a lista de vértices, serve para visualizar melhor quem é o pai de quem, e qual o vértice que se refere a lista de distâncias
        vertices[vertice - 1] = vertice # define o valor do vertice de origem na sua posição
        pais = [0] * self.numeroDeVertices() # inicializa a lista de pais
        pais[vertice - 1] = vertice # define a origem como pai dela mesma
        
        for i in range(self.numeroDeVertices()):
            for valor in self.lista_de_adjacencia[i + 1]: # percorre os vizinhos de cada vertice
                u, v, p = i + 1, valor[0], valor[1]
                if dist[u-1] != float("Inf") and dist[u-1] + p <= dist[v-1]: # confere quem tem a menor distância
                    dist[v-1] = dist[u-1] + p # atualiza a distância
                    vertices[v-1] = v 
                    pais[v-1] = u # atualiza o pai
        
        i = 0
        for valor in self.lista_de_adjacencia[i + 1]: 
            u, v, p = i + 1, valor[0], valor[1]
            i = i + 1
            if dist[u] != float("Inf") and dist[u] + p < dist[v]: # confere se tem ciclo negativo no grafo
                print("Grafo contém ciclo negativo.")
                return
 
        return vertices, dist, pais
    
    # utiliza dijkstra para procurar o caminho mínimo de um vértice para todos os outros do grafo
    def dijkstra(self, vertice):
        dist = [float('inf')] * self.numeroDeVertices() # declara como infinita a distância dos vértices em relação a origem
        dist[vertice-1] = 0 # define como 0 a distância da origem
        
        pais = [0] * self.numeroDeVertices() # declara como 0 o pai de todos os vértices
        
        fila_de_prioridade = [] 
        heapq.heappush(fila_de_prioridade, (0, vertice)) # põe a origem no início da fila de prioridade
        
        while fila_de_prioridade: # vai percorrer enquanto tiver algum valor na fila
            d, u = heapq.heappop(fila_de_prioridade)
            
            for valor in self.lista_de_adjacencia[u]:
                v, p = valor[0], valor[1]
                if dist[v-1] > dist[u-1] + p: # confere quem tem maior distância
                    dist[v-1] = dist[u-1] + p # atualiza distância
                    pais[v-1] = u # atualiza o pai
                    heapq.heappush(fila_de_prioridade, (dist[v-1], v)) 
        
        return pais, dist
            
    # retorna o vértice mais distante do vértice desejado e sua distância
    def verticeMaisDistante(self, dist):
        # pais, dist = self.dijkstra(origem) 
        maior = max(dist)
        vertice = dist.index(maior) + 1

        return vertice, maior

        
    