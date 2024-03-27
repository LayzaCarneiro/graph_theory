from biblioteca.grafo import Grafo
from biblioteca.digrafo import Digrafo

# método para leitura do arquivo
def lerArquivo(path):
    arquivo = open(path, "r")
    arestas = []
    for linha in arquivo.readlines(): # percorre cada linha
        if linha[0] == "a": # se começar com a
            linha = linha.split()  
            arestas.append((int(linha[1]), int(linha[2]), int(linha[3])))  # adiciona na lista de arestas o vértice de origem, de destino e o peso da aresta
    return arestas

if __name__ == "__main__":
    _ = 1
    while(_):
        esc = int(input("Qual estrutura deseja utilizar? \n[1] Grafo \n[2] Digrafo \n\n>>>>>>  "))
        
        if(esc == 1):
            g = Grafo()
            _ = 0
        elif(esc == 2):
            g = Digrafo()
            _ = 0
        else:
            print("Escolha entre 1 e 2.")
    

    arestas = lerArquivo("USA-road-d.NY.gr")

    for aresta in arestas:
        g.adicionarAresta(aresta[0], aresta[1], aresta[2]) # adiciona cada aresta no digrafo
    

    # informações do grafo
    print("Quantidade de vértices: ", g.numeroDeVertices()) # resposta = 264346
    print("Quantidade de arestas: ", g.numeroDeArestas()) # resposta = 733846
    print("Grau Mínimo: ", g.menorGrau()) # resposta = 1
    print("Grau Máximo: ", g.maiorGrau()) # resposta = 8
    _, T = g.dijkstra(129)
    print("Vértice mais distante do vértice 129 e sua distância: ", g.verticeMaisDistante(T)) # resposta = 90644, 1437303 (vértice, distância)
    