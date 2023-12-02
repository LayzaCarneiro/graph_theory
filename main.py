from grafo import Grafo

# estrutura = int(input("Informe sua estrutura de dados: \n[1] Grafo \n[2] Dígrafo \n"))

grafo = Grafo()
grafo.inserirVertice(1)
grafo.inserirVertice(2)
grafo.inserirVertice(3)
grafo.adicionarConexao(1, 3)
grafo.adicionarConexao(3, 2, 5)

print(grafo.numeroDeArestas())
print(grafo.numeroDeVertices())
print(grafo.vizinhos(3))

# G = biblioteca.Grafo() or biblioteca.Digrafo()
# G.adicionarConexao = (x, y) // x é origem e y é destino, e peso é o padrão
# G.adicionarConexao = (x, y, peso=100) // aqui é o peso é escolhido