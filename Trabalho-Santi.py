# 1 - Busca em Largura em cima de uma lista de adjacencia
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def busca_em_largura_padrao(grafo, inicio):
    visitados = [inicio]
    fila = [inicio]

    while len(fila) > 0:
        atual = fila.pop(0)
        print("Visitando:", atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return visitados


# 2 - Busca de menor caminho utilizando Busca em Largura
def busca_em_largura_menor_caminho(grafo, inicio, fim):
    visitados = [inicio]
    fila = [[inicio]]

    while len(fila) > 0:
        caminho = fila.pop(0)
        atual = caminho[-1]

        if atual == fim:
            return caminho

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                novo_caminho = caminho + [vizinho]
                fila.append(novo_caminho)

    return None


print("Busca em Largura Padrao:")
ordem = busca_em_largura_padrao(grafo, "A")
print("Ordem final:", ordem)

print()
print("Busca em Largura para Menor Caminho:")
caminho = busca_em_largura_menor_caminho(grafo, "A", "F")
print("Menor caminho de A ate F:", caminho)
