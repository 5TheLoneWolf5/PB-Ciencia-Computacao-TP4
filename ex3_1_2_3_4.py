class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

def dfs(lista_adjacencia, vertice, visitados=None):
    if visitados is None:
        visitados = set()

    print(vertice, end=" ")
    visitados.add(vertice)

    for vizinho in lista_adjacencia[vertice]:
        if vizinho not in visitados:
            dfs_recursivo(lista_adjacencia, vizinho, visitados)

def bfs(lista_adjacencia, inicio):
    visitados = set()
    fila = [inicio]

    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            print(vertice, end=" ")
            visitados.add(vertice)
            for vizinho in lista_adjacencia[vertice]:
                if vizinho not in visitados:
                    fila.append(vizinho)

def bfs_path(lista_adjacencia, inicio, objetivo):
    visitados = set()
    fila = [(inicio, [inicio])]

    while fila:
        vertice, caminho = fila.pop(0)
        if vertice not in visitados:
            if vertice == objetivo:
                print(f"\n{objetivo} encontrado!")
                return caminho
            visitados.add(vertice)

            for vizinho in lista_adjacencia[vertice]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    print("\nCaminho não encontrado.")
    return None

grafo = Grafo()

for v in ["A", "B", "C", "D", "E"]:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

dfs(grafo.lista_adjacencia, "A")
print()
bfs(grafo.lista_adjacencia, "A")
print(bfs_path(grafo.lista_adjacencia, "A", "E"))