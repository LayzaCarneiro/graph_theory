# Trabalho - Biblioteca de Grafos em Python
Trabalho da cadeira de Teoria dos Grafos sobre estrutura de dados para grafos utilizando Python.

+ A biblioteca contém duas classes: uma correspondente à estrutura de dados "Grafo" e outra à "Digrafo".
+ A biblioteca fornece os seguintes métodos para ambas as classes:

<table>
  <tr>
    <th>Método</th>
    <th>Retorno</th>
  <tr>
    <td>G.n</td>
    <td>Número de vértices do grafo</td>
  </tr>
  <tr>
    <td>G.m</td>
    <td>Número de arestas do grafo</td>
  </tr>
  <tr>
    <td>G.viz(v)</td>
    <td>Vizinhaça do vértice v</td>
  </tr>
  <tr>
    <td>G.d(v)</td>
    <td>Grau do vértice v</td>
  </tr>
  <tr>
    <td>G.w(uv)</td>
    <td>Peso da aresta uv</td>
  </tr>
  <tr>
    <td>G.mind</td>
    <td>Menor grau presente no grafo</td>
  </tr>
  <tr>
    <td>G.maxd</td>
    <td>Maior grau presente no grafo</td>
  </tr>
  <tr>
    <td>G.bfs(v)</td>
    <td>Executa uma busca em largura (BFS) a partir do vértice v e retorna duas listas: "distância" - representa a distância entre cada vértice e v - e "pi" - armazena o vértice predecessor (pai) no caminho de v até cada vértice</td>
  </tr>
  <tr>
    <td>G.dfs(v)</td>
    <td>Executa uma busca em profundidade (DFS) a partir do vértice v e retorna três listas: "pi" - armazena o vértice predecessor na árvore de busca, "v.ini" - indica o tempo de início da visita a cada vértice e "v.fim" - indicia o tempo de término da visita a cada vértice</td>
  </tr>
  <tr>
    <td>G.bf(v)</td>
    <td>Executa o algoritmo de Bellman-Ford a partir do vértice v como origem. Retorna duas listas: "distância" - representa as distâncias mínimas entre v e cada vértice e "pi" - armazena o vértice predecessor (pai) do caminho mínimo de v até cada vértice</td>
  </tr>
  <tr>
    <td>G.dijkstra(v)</td>
    <td>Executa o algoritmo de Dijkstra a partir do vértice v como origem. Retorna duas listas:  "distância" - representa as distâncias mínimas entre v e cada vértice e "pi" - armazena o vértice predecessor (pai) do caminho mínimo de v até cada vértice</td>
  </tr>
</table>
